from django.shortcuts import render,HttpResponse,redirect
from .models import Post
from Posts.forms import EmailForm,ContactForm
from django.core.paginator import Paginator ,EmptyPage, PageNotAnInteger
# Create your views here.

def blog_home(request):
    posts = Post.objects.filter(status=1)
    paginator = Paginator(posts, 3)
    try:
        page_number = request.GET.get("page")
        posts = paginator.get_page(page_number)
    except EmptyPage:
        posts = paginator.get_page(1)
    except PageNotAnInteger:
        posts = paginator.get_page(1)
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
def contact(request):
    return render(request, 'blog/contact.html')

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('/')        
            