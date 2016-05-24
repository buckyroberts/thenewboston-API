from rest_framework.response import Response
from rest_framework.views import APIView
from v1.models import Major
from v1.serializers import MajorSerializer


# majors/
class MajorView(APIView):

    @staticmethod
    def get(request):
        majors = Major.objects.all()
        serializer = MajorSerializer(majors, many=True)
        return Response(serializer.data)
