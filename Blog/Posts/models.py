from django.db import models
from django.contrib.auth.models import User
# post blog model
      
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length = 300)
    content = models.TextField()
    image = models.ImageField(upload_to="blogs", default='default.jpg')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    content_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now = True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ["-published_date"]


class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    news_status = models.BooleanField(default=True)
    
    
    def __str__(self) -> str:
        return self.email
    
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.subject