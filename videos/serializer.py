from rest_framework import serializers
from videos.models import Categoria, Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'titulo', 'descricao', 'url', 'categoria_id']
        
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'titulo', 'cor']