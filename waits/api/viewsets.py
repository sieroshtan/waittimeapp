from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from .serializers import WaitSerializer, WaitRatingPathSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnObject
from ..models import Wait


class WaitViewSet(viewsets.ModelViewSet):
    queryset = Wait.objects.all()
    serializer_class = WaitSerializer
    permission_classes = [IsAuthenticated, IsOwnObject]
    model = Wait

    def update(self, request, *args, **kwargs):
        return super(WaitViewSet, self).update(request, partial=True)

    def create(self, request, *args, **kwargs):
        if request.user.waits_for_user.filter(end_time__isnull=True, star_time__lte=timezone.now() + timedelta(hours=24)).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'non_field_errors': "User already have the started wait"})
        return super(WaitViewSet, self).create(request, *args, **kwargs)

    @list_route()
    def clear(self, request):
        time_threshold = datetime.now() - timedelta(hours=24)
        Wait.objects.filter(end_time__isnull=True, star_time__lte=time_threshold).delete()
        return Response(status.HTTP_200_OK)

    @detail_route(methods=['post'])
    def end(self, request, pk=None):
        wait = self.get_object()
        serializer = WaitRatingPathSerializer(wait, data=request.data)
        if serializer.is_valid():
            wait = serializer.save()
            wait.end_time = timezone.now()
            wait.total_time = (wait.end_time - wait.star_time).seconds / 60
            wait.save()

            user = wait.user
            user.number_of_wait_samples = user.waits_for_user.filter(total_time__isnull=False).count()
            waits_total_times = [w.total_time for w in user.waits_for_user.filter(total_time__isnull=False)]
            user.total_wait = sum(waits_total_times) / len(waits_total_times)
            user.save()

            location = wait.location
            location.number_of_wait_samples = location.waits_for_location.filter(total_time__isnull=False).count()
            waits_total_times = [w.total_time for w in location.waits_for_location.filter(total_time__isnull=False)]
            location.total_wait = sum(waits_total_times) / len(waits_total_times)
            location.rating = (location.rating + wait.rating) / 2 if location.rating else wait.rating
            location.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)
