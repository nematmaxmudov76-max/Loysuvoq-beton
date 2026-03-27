from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.common.models import Media
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from apps.common.apis.serializers import MediaSerializer
from apps.common.models import Media, State, Region, Currency

class CommonPostListAPIView(APIView):
    def get(self, request):
        media = Media.objects.all()
        serializer = MediaSerializer(media, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = MediaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class CommonMediaListAPIView(ListAPIView):
    queryset = Media.objects.all().order_by("-created_at")
    serializer_class = MediaSerializer

class CommonMediaDetailApiView(RetrieveAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class CommonMediaCreateApiView(CreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class CommonMediaUpdateApiView(UpdateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class CommonMediaDeleteApiView(DestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer