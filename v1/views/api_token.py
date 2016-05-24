from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from v1.models import ApiToken
from v1.serializers import ApiTokenSerializer


# api_tokens/{token}/
@api_view(['GET'])
def view_single_token(request, token):
    row = get_object_or_404(ApiToken, token=token)
    serializer = ApiTokenSerializer(row)
    return Response(serializer.data)
