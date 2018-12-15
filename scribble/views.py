from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comment
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request,'post_detail.html',{'post': post})
