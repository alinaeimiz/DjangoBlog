from django import template
from Posts.models import *
register = template.Library()

@register.inclusion_tag('wiget/popular-post.html')
def popular_post():
    posts = Post.objects.filter(status = 1)[:4]
    return {'posts':posts}