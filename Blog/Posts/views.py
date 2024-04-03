from django.shortcuts import render,HttpResponse,redirect
from .models import Post
from Posts.forms import EmailForm

# Create your views here.

def blog_home(request):
    posts = Post.objects.filter(status=1)
    return render(request, 'blog/blog-home.html',{'posts':posts})
    
    
def single(request,page):
    single = Post.objects.filter(status=1).filter(id=page)
    return render(request, 'blog/blog-single.html',{'single':single})

def search(request):
    posts = Post.objects.filter(status = 1)
    if request.method == 'GET':
        if q := request.GET.get('q'):
            posts = posts.filter(content__contains = q)      
    return render(request,'blog/blog-home.html', {'posts':posts})

def search_category(request,cat):
    posts = Post.objects.filter(status = 1)
    if request.method == 'GET':
        posts = posts.filter(category__name=cat)
    return render(request,'blog/blog-home.html', {'posts':posts})


def newsletter(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('/')
    
            
            