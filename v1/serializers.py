from rest_framework import serializers
from .models import ApiToken, Major, Course, Video


class ApiTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApiToken
        fields = '__all__'


class MajorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Major
        exclude = ('id',)


class CourseSerializer(serializers.ModelSerializer):
    major = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('id', 'name', 'category', 'major')

    def get_major(self, course):
        return course.major.slug


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        exclude = ('id',)
