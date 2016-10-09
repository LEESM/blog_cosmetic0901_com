from django.contrib import admin
from .models import Category, Post
from django_summernote.admin import SummernoteModelAdmin

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['category_name','url_name', 'order',]

class PostAdmin(SummernoteModelAdmin):
	list_display = ['subject','description','url_name','content', 'image', 'author', 'category', 'pub_date']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
