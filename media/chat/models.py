from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

def upload_image_to(instance,filename):
	return f'message_media/{instance}/{filename}'  

def upload_video_to(instance,filename):
	return f'video/{instance}/{filename}'  


class Message(models.Model):

    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    message = models.TextField(null = True)
  
    images = models.ImageField( null = True, blank = True, default=False, upload_to=upload_image_to,)
    video = models.FileField(null = True, blank = True, default=False, upload_to=upload_image_to)
    seen = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("date_created",)