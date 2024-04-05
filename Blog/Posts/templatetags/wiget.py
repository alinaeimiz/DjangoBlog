from django import template
from Posts.models import *
register = template.Library()

@register.inclusion_tag('wiget/popular-post.html')
def popular_post():
    posts = Post.objects.filter(status = 1)[:4]
    return {'posts':posts}


@register.inclusion_tag("wiget/post-category.html")
def post_category():
    posts = Post.objects.filter(status=1)
    category = Category.objects.all()
    counts={}
    for name in category:
         counts[name] = posts.filter(category=name).count()
    
    return {"counts":counts}

@register.inclusion_tag("wiget/cloud.html")
def cloud():
    category = Category.objects.all() 
    return {'category':category}



    