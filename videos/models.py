from django.db import models

class Videos(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=1000)
    url = models.CharField(max_length=200)
    
    def __str__(self):
        return self.titulo
