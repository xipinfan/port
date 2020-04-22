from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.

def blog(request):
    text = Blog.objects.all()
    return render(request, 'blog.html', context={'text': text})

def text1(request, blog_id):
    text2 = get_object_or_404(Blog, pk=blog_id)
    #text2 = Blog.objects.all()[blog_id-1]
    return render(request, 'blog_text.html',{'text': text2})