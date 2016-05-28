from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.models import ApiToken, Course, Major
from v1.serializers import CourseSerializer


# {major_slug}/
class CourseView(APIView):

    @staticmethod
    def get(request, major_slug):
        major = get_object_or_404(Major, slug=major_slug)
        courses = Course.objects.filter(major=major)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request, major_slug):
        if not ApiToken.objects.filter(token=request.data['token'], is_master=True):
            return Response({'Invalid': 'You do not have create permissions'}, status=status.HTTP_403_FORBIDDEN)
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @staticmethod
    def delete(request, major_slug):
        if not ApiToken.objects.filter(token=request.data['token'], is_master=True):
            return Response({'Invalid': 'You do not have create permissions'}, status=status.HTTP_403_FORBIDDEN)
        course = Course.objects.filter(id=request.data['id'])
        if course:
            course[0].delete()
            return Response({'Success': 'Course deleted'}, status=status.HTTP_200_OK)
        return Response({'Invalid': 'That course does not exist'}, status=status.HTTP_200_OK)
