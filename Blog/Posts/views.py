from django.shortcuts import render
from .models import Post
# Create your views here.
def blog_home(request):
    posts = Post.objects.filter(status=1)
    return render(request, 'blog/blog-home.html',{'posts':posts})
    
    
def single(request):
    return render(request, 'blog/blog-single.html')