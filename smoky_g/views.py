from django.shortcuts import render
from blog.models import Blog, Product


def home(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'index.html', context)


def blog(request):
    blogs = Blog.objects.filter(status="Published")
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog.html', context)
