from rest_framework.response import Response
from rest_framework.views import APIView
from v1.models import Course
from v1.serializers import CourseSerializer


# courses/
class CourseView(APIView):

    @staticmethod
    def get(request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
