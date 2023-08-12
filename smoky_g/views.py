from django.shortcuts import render
from blog.models import Blog


def home(request):
    return render(request, 'index.html')


def blog(request):
    blogs = Blog.objects.filter(status="Published")
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog.html', context)