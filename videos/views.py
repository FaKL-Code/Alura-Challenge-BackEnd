from rest_framework import viewsets
from videos.models import Categorias, Videos
from videos.serializer import CategoriaSerializer, VideoSerializer

class VideosViewSet(viewsets.ModelViewSet):

    queryset = Videos.objects.all()

    def get_serializer_class(self):
        return VideoSerializer
    
    def get_queryset(self):
        titulo = self.request.query_params.get("search")
        if titulo:    
            qs = Videos.objects.filter(titulo__contains=titulo)
        else:
            qs = self.queryset
        return qs

class CategoriasViewSet(viewsets.ModelViewSet):
    
    queryset = Categorias.objects.all()
    
    def get_serializer_class(self):
        return CategoriaSerializer
    
class CategoriasVideosViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        categoria_id = self.kwargs['pk']
        if categoria_id:    
            result = Videos.objects.filter(categoria_id=categoria_id)
            return result
        else:
            raise ValueError('objeto nao existe')
        
    def get_serializer_class(self):
        return VideoSerializer
        