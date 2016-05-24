from rest_framework.response import Response
from rest_framework.views import APIView
from v1.models import Playlist
from v1.serializers import PlaylistSerializer


# playlists/
class PlaylistView(APIView):

    @staticmethod
    def get(request):
        pages = Playlist.objects.all()
        serializer = PlaylistSerializer(pages, many=True)
        return Response(serializer.data)
