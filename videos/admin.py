from django.contrib import admin
from videos.models import Video, Categoria

class Videos(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'url')
    list_display_links = ('id', 'titulo')
    search_fields = ('id', 'titulo')
    list_per_page = 30
    
admin.site.register(Video, Videos)

class Categorias(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'cor')
    list_display_links = ('id', 'titulo')
    search_fields = ('id', 'titulo')
    list_per_page = 30
    
admin.site.register(Categoria, Categorias)
