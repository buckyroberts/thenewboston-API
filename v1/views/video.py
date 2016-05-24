from rest_framework.response import Response
from rest_framework.views import APIView
from v1.models import Video
from v1.serializers import VideoSerializer


# video/
class VideoView(APIView):

    @staticmethod
    def get(request):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
