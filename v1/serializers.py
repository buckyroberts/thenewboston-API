from rest_framework import serializers
from .models import ApiToken, Subject, Playlist, Video


class ApiTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApiToken
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'


class PlaylistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Playlist
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        exclude = ('id',)
