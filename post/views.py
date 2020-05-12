from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.

def index(request):
    post_list = Post.objects.all()[::-1]
    return render(request, "index.html", {'posts': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "detail.html", {'post': post})
