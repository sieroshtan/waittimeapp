from django.conf.urls import url, include
from rest_framework import routers
from api.viewsets import LocationViewSet

router = routers.SimpleRouter()
router.register(r'locations', LocationViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
