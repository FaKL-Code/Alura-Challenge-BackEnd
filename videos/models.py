from django.db import models

class Videos(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    titulo = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=1000, null=False)
    url = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.titulo
