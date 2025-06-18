# Create your views here.
# def recepies(request):
#     return render(request, 'recepie.html')

from django.shortcuts import render, get_object_or_404
from .models import Blog

def recepies(request):
    blogs = Blog.objects.all()
    return render(request, 'recepie.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})
