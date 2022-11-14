from django.db import models

class Videos(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    titulo = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=1000, null=False)
    url = models.CharField(max_length=200, null=False)
    categoria_id = models.IntegerField(models.ForeignKey("videos.Categorias", verbose_name=(""), on_delete=models.CASCADE), default=1)
    
    def __str__(self):
        return self.titulo
    
class Categorias(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    titulo = models.CharField(max_length=30, null=False)
    cor = models.CharField(max_length=20, null=False)
    
    def __str__(self):
        return self.titulo
