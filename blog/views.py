from django.shortcuts import render
from .models import Blog
# Create your views here.

def blog(request):
    text = Blog.objects.all()
    return render(request, 'blog.html', context={'text': text})