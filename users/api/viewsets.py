from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import UserSerializer, PasswordSerializer
from .permissions import IsCreationOrIsAuthenticated, IsOwner


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsCreationOrIsAuthenticated, IsOwner]
    model = get_user_model()
    lookup_field = 'username'

    @detail_route(methods=['post'])
    def set_password(self, request, username=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=['post'])
    def revoke_token(self, request, username=None):
        user = self.get_object()
        user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        return super(UserViewSet, self).update(request, partial=True)
