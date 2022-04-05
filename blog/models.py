import django
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


from blog import migrations

# Create your models here.
class PublishedManager(models.Manager):
       def published(self):
          return super(PublishedManager,self).get_queryset().filter()


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(null=False, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    body = models.TextField()
    published_on = models.DateTimeField(auto_now_add =True)
    published= models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    objects = PublishedManager()


    class Meta:
        ordering = ['-published_on']

    def __str__(self):
        return self.title

