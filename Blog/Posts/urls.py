from django.urls import path
from . import views
app_name = 'post'


urlpatterns = [
    path('', views.blog_home, name='blog-home'),
    path('<int:page>/', views.single, name='single'),
    path('search/',views.search, name='search'),
    path('category/<str:cat>', views.search_category, name='search-category'),
    path('newsletter',views.newsletter, name='newsletter'),
]