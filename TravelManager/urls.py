from rest_framework import routers
from .views import ProjectViewSet, PlaceViewSet, ProjectPlaceViewSet

router = routers.DefaultRouter()

router.register(r'projects', ProjectViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'projects-places', ProjectPlaceViewSet)

urlpatterns = router.urls