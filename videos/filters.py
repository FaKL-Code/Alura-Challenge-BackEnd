from videos.models import Videos

def video_filter(categoria_id):
    
    return Videos.objects.filter(categoria_id=categoria_id)
