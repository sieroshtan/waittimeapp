import datetime
from math import cos, degrees, radians
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from .serializers import LocationSerializer
from ..models import Location
from waits.models import Wait
from waits.api.serializers import WaitSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    model = Location

    def get_queryset(self):
        queryset = Location.objects.all()

        type = self.request.query_params.get('type', None)
        radius = self.request.query_params.get('radius', None)
        lat = self.request.query_params.get('lat', None)
        lon = self.request.query_params.get('lon', None)

        if type and radius and lat and lon:
            radius = float(radius)
            lat = float(lat)
            lon = float(lon)

            r = 6371  # Earth radius in km

            lat_range = degrees(radius / r)
            lon_range = degrees(radius / (r * cos(radians(lat))))

            min_lat = lat - lat_range
            max_lat = lat + lat_range
            min_lon = lon - lon_range
            max_lon = lon + lon_range

            queryset = queryset.filter(type=type,
                                       latitude__range=(min_lat, max_lat),
                                       longitude__range=(min_lon, max_lon))[:5]

        return queryset

    def update(self, request, *args, **kwargs):
        return super(LocationViewSet, self).update(request, partial=True)

    @detail_route()
    def last_waits(self, request, pk=None):
        location = self.get_object()

        hours = request.query_params.get('hours', 2)

        date_from = datetime.datetime.now() - datetime.timedelta(hours=hours)
        waits = Wait.objects.filter(location=location, end_time__gte=date_from)
        wait_serializer = WaitSerializer(waits, many=True)
        return Response(data=wait_serializer.data)
