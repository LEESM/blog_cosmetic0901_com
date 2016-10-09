from django.db import models
from django.conf import settings

def upload_to(instance, filename):
    path_arr = filename.split('/')
    return 'user/%s/%s' %(instance.user.username, path_arr[-1])

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
	nick = models.CharField(max_length=50, blank=True,)
	thumbnail = models.ImageField(blank=True, upload_to=upload_to)
