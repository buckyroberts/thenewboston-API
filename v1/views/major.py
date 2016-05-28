from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from v1.models import ApiToken, Major
from v1.serializers import MajorSerializer


# majors/
class MajorView(APIView):

    @staticmethod
    def get(request):
        majors = Major.objects.all()
        serializer = MajorSerializer(majors, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        if not ApiToken.objects.filter(token=request.data['token'], is_master=True):
            return Response({'Invalid': 'You do not have create permissions'}, status=status.HTTP_403_FORBIDDEN)
        serializer = MajorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request):
        if not ApiToken.objects.filter(token=request.data['token'], is_master=True):
            return Response({'Invalid': 'You do not have create permissions'}, status=status.HTTP_403_FORBIDDEN)
        major = Major.objects.filter(slug=request.data['slug'])
        if major:
            major[0].delete()
            return Response({'Success': 'Major deleted'}, status=status.HTTP_200_OK)
        return Response({'Invalid': 'That major does not exist'}, status=status.HTTP_200_OK)
