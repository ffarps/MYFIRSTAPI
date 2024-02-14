from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import IteamSerializer

@api_view(['GET'])
def getData(request):
    items=Item.objects.all()
    serializer=IteamSerializer(items,many=True)
    return Response(serializer.data)
