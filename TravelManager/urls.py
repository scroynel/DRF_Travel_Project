from django.urls import path, include
from rest_framework import routers
from .views import ProjectViewSet, PlaceViewSet, ProjectPlaceViewSet, ProjectPlacesView

router = routers.DefaultRouter()

router.register(r'projects', ProjectViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'projects-places', ProjectPlaceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('projects/<int:project_id>/places/', ProjectPlacesView.as_view(), name='project_places')
]