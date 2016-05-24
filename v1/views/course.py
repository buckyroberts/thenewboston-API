from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.models import Course, Major
from v1.serializers import CourseSerializer


# courses/computer-science/
class CourseView(APIView):

    @staticmethod
    def get(request, major_slug):
        major = get_object_or_404(Major, slug=major_slug)
        courses = Course.objects.filter(major=major)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
