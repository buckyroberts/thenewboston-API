from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.models import Course, Video
from v1.serializers import VideoSerializer


# videos/{course_id}/
class VideoView(APIView):

    @staticmethod
    def get(request, course_id):
        course = get_object_or_404(Course, id=course_id)
        videos = Video.objects.filter(course=course)
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
