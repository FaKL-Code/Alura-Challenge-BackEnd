from rest_framework import viewsets
from videos.models import Categorias, Videos
from videos.serializer import CategoriaSerializer, VideoSerializer
from videos.filters import video_filter

class VideosViewSet(viewsets.ModelViewSet):

    queryset = Videos.objects.all()

    def get_serializer_class(self):
        return VideoSerializer

class CategoriasViewSet(viewsets.ModelViewSet):
    
    queryset = Categorias.objects.all()
    
    def get_serializer_class(self):
        return CategoriaSerializer
    
class CategoriasVideosViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        categoria_id = self.kwargs['pk']
        if categoria_id:    
            result = video_filter(categoria_id=categoria_id)
            return result
        else:
            raise ValueError('objeto nao existe')
        
    def get_serializer_class(self):
        return VideoSerializer
        