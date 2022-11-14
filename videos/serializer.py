from rest_framework import serializers
from videos.models import Videos

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ['id', 'titulo', 'descricao', 'url']