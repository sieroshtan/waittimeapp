from django.conf.urls import url, include
from rest_framework import routers
from api.viewsets import WaitViewSet

router = routers.SimpleRouter()
router.register(r'waits', WaitViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
