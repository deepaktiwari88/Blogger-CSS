from django.shortcuts import render
from .models import Blog

def index(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/index.html', {'blogs':blogs})

def blog(request, pk):
    instance = Blog.objects.get(id=pk)
    return render(request, 'blog/main_blog.html', {'instance':instance})
