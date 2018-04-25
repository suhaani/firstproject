from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
def index(request):
	posts=Posts.objects.all()[:10]
	context={
			'title':'Latest Posts',
			'posts':posts
	}

	return render(request,'pages/index.html',context)

def details(request,id):
	post=Posts.objects.get(id=id)
	context={
			'post':post
			}
	return render(request,'pages/details.html',context)
# Create your views here.
