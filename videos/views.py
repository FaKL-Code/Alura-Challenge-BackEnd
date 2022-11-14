from rest_framework import viewsets
from videos.models import Categoria, Video
from videos.serializer import CategoriaSerializer, VideoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class VideosViewSet(viewsets.ModelViewSet):
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Video.objects.all()

    def get_serializer_class(self):
        return VideoSerializer
    
    def get_queryset(self):
        titulo = self.request.query_params.get("search")
        if titulo:    
            qs = Video.objects.filter(titulo__contains=titulo)
        else:
            qs = self.queryset
        return qs

class CategoriasViewSet(viewsets.ModelViewSet):
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Categoria.objects.all()
    
    def get_serializer_class(self):
        return CategoriaSerializer
    
class CategoriasVideosViewSet(viewsets.ModelViewSet):
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        categoria_id = self.kwargs['pk']
        if categoria_id:    
            result = Video.objects.filter(categoria_id=categoria_id)
            return result
        else:
            raise ValueError('objeto nao existe')
        
    def get_serializer_class(self):
        return VideoSerializer
        