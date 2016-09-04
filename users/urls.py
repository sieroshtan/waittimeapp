from django.conf.urls import url, include
from rest_framework import routers
from api.viewsets import UserViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
