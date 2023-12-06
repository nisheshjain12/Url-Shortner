from django.utils import timezone
from django.db import models

# Create your models here.

class Url(models.Model):
    url_id = models.AutoField(primary_key=True)
    link = models.CharField(max_length=100000000000)
    short_link = models.CharField(max_length=1000000)
    request_datetime = models.DateTimeField(default=timezone.now, blank=True)
    ip_address = models.CharField(max_length=50, default='127.0.0.1')  # Example default IP address


class Video(models.Model):
    embed_link = models.CharField(max_length=200)  # Field to store the YouTube video embed link

    
    def __str__(self):
        return self.embed_link
    
    @property
    def youtube_video_id(self):
        return self.get_youtube_video_id()

    def get_youtube_video_id(self):
        if 'youtube.com' in self.embed_link:
            try:
                video_id = self.embed_link.split('v=')[1].split('&')[0]
                return video_id
            except IndexError:
                return None
        return None
    