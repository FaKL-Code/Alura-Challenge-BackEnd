from rest_framework import viewsets
from videos.models import Categorias, Videos
from videos.serializer import CategoriaSerializer, VideoSerializer


class VideosViewSet(viewsets.ModelViewSet):

    queryset = Videos.objects.all()

    def get_serializer_class(self):
        return VideoSerializer

class CategoriasViewSet(viewsets.ModelViewSet):
    
    queryset = Categorias.objects.all()
    
    def get_serializer_class(self):
        return CategoriaSerializer