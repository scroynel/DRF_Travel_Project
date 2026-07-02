from rest_framework import serializers
from .models import Project, Place, ProjectPlace


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class ProjectPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPlace
        fields = '__all__'


class ProjectPlacesSerializer(serializers.ModelSerializer):
    place_name = serializers.CharField(source='place.title', read_only=True)


    class Meta:
        model = ProjectPlace
        fields = ('id', 'place', 'place_name', 'notes', 'visited')
        read_only_fields = ('place', )