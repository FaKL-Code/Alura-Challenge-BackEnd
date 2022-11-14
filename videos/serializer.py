from rest_framework import serializers
from videos.models import Categorias, Videos

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ['id', 'titulo', 'descricao', 'url', 'categoria_id']
        
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = ['id', 'titulo', 'cor']