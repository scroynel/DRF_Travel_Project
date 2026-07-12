from rest_framework import viewsets, exceptions, generics
from .models import Project, Place, ProjectPlace
from .serializers import ProjectSerializer, PlaceSerializer, ProjectPlaceSerializer, ProjectPlacesSerializer, ProjectPlacesUpdateSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.places.filter(visited=True).exists():
            raise exceptions.ValidationError(f'Cannot delete Project - {obj.name} with visited places')
        return super().destroy(request, *args, **kwargs)


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class ProjectPlaceViewSet(viewsets.ModelViewSet):
    queryset = ProjectPlace.objects.all()
    serializer_class = ProjectPlaceSerializer


class ProjectPlacesView(viewsets.ModelViewSet):
    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return ProjectPlace.objects.filter(project_id=project_id)
    

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return ProjectPlacesUpdateSerializer
        return ProjectPlacesSerializer


    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['project_id'] = self.kwargs['project_id']
        return context