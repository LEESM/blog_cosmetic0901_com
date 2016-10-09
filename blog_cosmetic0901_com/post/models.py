from django.db import models
from django.conf import settings

class Category(models.Model):
	category_name = models.CharField(max_length=50)
	url_name = models.CharField(max_length=50, blank=True, default='')
	order = models.IntegerField(default=0)

	def __str__(self):
		return self.category_name

def upload_to(instance, filename):
    path_arr = filename.split('/')
    return 'post/%s/%s' %(instance.subject, path_arr[-1])

class Post(models.Model):
	subject = models.CharField(max_length=100)
	description = models.CharField(max_length=100,blank=True)
	url_name = models.CharField(max_length=100, blank=True, default='')
	content = models.TextField(blank=True)
	image = models.ImageField(blank=True, upload_to=upload_to)
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	category = models.ForeignKey(Category,blank=True, null=True,on_delete=models.SET_NULL)
	pub_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.subject
