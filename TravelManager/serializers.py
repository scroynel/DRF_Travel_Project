from rest_framework import serializers
from .models import Project, Place, ProjectPlace
from .services.artic import fetch_place_from_api


class ProjectSerializer(serializers.ModelSerializer):
    places = serializers.ListField(write_only=True, required=False)


    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'start_date', 'places')


    def create(self, validated_data):
        external_ids = validated_data.pop('places', [])

        project = Project.objects.create(**validated_data)

        for external_id in external_ids:
            place = Place.objects.filter(external_id=external_id).first()
            if not place:
                response = fetch_place_from_api(external_id)
                
                if not response:
                    raise serializers.ValidationError('Place {external_id} not found in external API')

                place = Place.objects.create(
                    external_id = external_id,
                    title = response['data']['title']
                )

            ProjectPlace.objects.create(
                project = project,
                place = place
            )

        return project


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class ProjectPlaceSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M')


    class Meta:
        model = ProjectPlace
        fields = ('project', 'place', 'notes', 'visited', 'created_at')


class ProjectPlacesSerializer(serializers.ModelSerializer):
    place_name = serializers.CharField(source='place.title', read_only=True)


    class Meta:
        model = ProjectPlace
        fields = ('id', 'place', 'place_name', 'notes', 'visited')
        read_only_fields = ('place', )