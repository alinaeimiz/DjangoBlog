from django.urls import path
from . import views
app_name = 'post'


urlpatterns = [
    path('', views.blog_home, name='blog-home'),
    path('single/', views.single, name='single'),
]