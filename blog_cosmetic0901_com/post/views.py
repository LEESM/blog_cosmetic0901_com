from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, HttpResponse, get_object_or_404
from post.models import Post, Category
from django.http import Http404

def index(request):
	posts_raw = Post.objects.all().order_by('-pub_date')
	paginator = Paginator(posts_raw, 5)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request,"post/index.html",{'posts':posts, 'title':'화장품연구공원 공식 블로그 - blog.cosmetic0901.com'})

def category(request,url_name):
	try:
		category = Category.objects.get(url_name=url_name)
	except Category.DoesNotExist:
		raise Http404("Category does not exist")
	posts_raw = Post.objects.filter(category=category).order_by('-pub_date')
	paginator = Paginator(posts_raw, 5)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request,"post/index.html",{'posts':posts,'category':category, 'title':category })

def post(request,url_name):
	post = get_object_or_404(Post, url_name=url_name)
	return render(request, "post/post.html", {'post':post, 'title':post.subject,})