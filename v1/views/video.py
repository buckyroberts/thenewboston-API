from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.models import ApiToken, Course, Video
from v1.serializers import VideoSerializer


# videos/{course_id}/
class VideoView(APIView):

    @staticmethod
    def get(request, course_id):
        course = get_object_or_404(Course, id=course_id)
        videos = Video.objects.filter(course=course)
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        if not ApiToken.objects.filter(token=request.data['token'], is_master=True):
            return Response({'Invalid': 'You do not have create permissions'}, status=status.HTTP_403_FORBIDDEN)
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request):
        if not ApiToken.objects.filter(token=request.data['token'], is_master=True):
            return Response({'Invalid': 'You do not have create permissions'}, status=status.HTTP_403_FORBIDDEN)
        course = Course.objects.filter(id=request.data['id'])
        if course:
            course[0].delete()
            return Response({'Success': 'Course deleted'}, status=status.HTTP_200_OK)
        return Response({'Invalid': 'That course does not exist'}, status=status.HTTP_200_OK)
