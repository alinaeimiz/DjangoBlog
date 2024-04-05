from django.shortcuts import render
from Posts.models import *
# Create your views here.
def home(request):
    posts = Post.objects.filter(status = 1)
    return render(request, 'home/index.html', {'posts':posts[:8]})