 #Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Blog
import markdown
from django.utils.safestring import mark_safe


def recepies(request):
    blogs = Blog.objects.all().order_by('-created_at')  # latest first
    return render(request, 'blog.html', {'blogs': blogs})

def second(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.content = mark_safe(markdown.markdown(blog.content))
    return render(request, 'blog_detail.html', {'blog': blog})

