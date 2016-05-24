from rest_framework.response import Response
from rest_framework.views import APIView
from v1.models import Subject
from v1.serializers import SubjectSerializer


# subjects/
class SubjectView(APIView):

    @staticmethod
    def get(request):
        pages = Subject.objects.all()
        serializer = SubjectSerializer(pages, many=True)
        return Response(serializer.data)
