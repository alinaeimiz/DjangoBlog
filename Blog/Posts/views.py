from django.shortcuts import render

# Create your views here.
def blog_home(request):
    return render(request, 'blog/blog-home.html')
    
    
def test(request):
    return render(request, 'base.html')