from rest_framework import viewsets
from videos.models import Videos
from videos.serializer import VideoSerializer


class VideosViewSet(viewsets.ModelViewSet):

    queryset = Videos.objects.all()

    def get_serializer_class(self):
        return VideoSerializer
