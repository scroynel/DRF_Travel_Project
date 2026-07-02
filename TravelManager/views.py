from rest_framework import viewsets, exceptions
from .models import Project, Place, ProjectPlace
from .serializers import ProjectSerializer, PlaceSerializer, ProjectPlaceSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.place.filter(visited=True).exists():
            raise exceptions.ValidationError(f'Cannot delete Project - {obj.name} with visited places')
        return super().destroy(request, *args, **kwargs)


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class ProjectPlaceViewSet(viewsets.ModelViewSet):
    queryset = ProjectPlace.objects.all()
    serializer_class = ProjectPlaceSerializer