from rest_framework import serializers
from .models import ApiToken, Major, Course, Video


class ApiTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApiToken
        fields = '__all__'


class MajorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Major
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        exclude = ('id',)
