from django.db import models
from django.conf import settings

class Category(models.Model):
	category_name = models.CharField(max_length=50)
	order = models.IntegerField(default=0)

	def __str__(self):
		return self.category_name

def get_image_path(instance, filename):
	return os.path.join('item_images', str(instance.item_id), filename)

class Post(models.Model):
	subject = models.CharField(max_length=100)
	description = models.CharField(max_length=100,blank=True)
	content = models.TextField(blank=True)
	image = models.ImageField(blank=True, upload_to=get_image_path)
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	category = models.ForeignKey(Category,blank=True, null=True,on_delete=models.SET_NULL)
	pub_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.subject
