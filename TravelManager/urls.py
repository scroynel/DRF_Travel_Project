from django.urls import path, include
from rest_framework import routers
from .views import ProjectViewSet, PlaceViewSet, ProjectPlaceViewSet, ProjectPlacesView

router = routers.DefaultRouter()

router.register(r'projects', ProjectViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'projects-places', ProjectPlaceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('projects/<int:project_id>/places/', ProjectPlacesView.as_view({'get': 'list'}), name='project_places'),
    path('projects/<int:project_id>/places/<int:pk>/', ProjectPlacesView.as_view({'get': 'retrieve', 'put': 'update'}), name='project_place')
]