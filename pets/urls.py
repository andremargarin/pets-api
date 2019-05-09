from django.conf.urls import url, include
from rest_framework import routers
from .views import PersonViewSet, PetViewSet


router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)
router.register(r'pet', PetViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
