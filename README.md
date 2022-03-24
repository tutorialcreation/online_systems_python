# Online System
# Flexy
In this course we shall be building an online system called Flexy

Task 1:
create an isolated environment
```python
python3 -m venv env
```
Task 2:
activate your virtual environment
```python
source env/bin/activate
```

Task 3:
install django, because I have already set up the requirements for you
perform the following command
```python
python -m pip install -r requirements.txt
```

Task 4:
spin up your first project
```python
django-admin startproject flexy
```

Task 5:
migrate your models into your database schema
```python
cd flexy
python manage.py migrate 
```

Task 6:
our system shall have a blog so let us create an application called blog
```python
python manage.py startapp blog
```

Task 7:
view the system interface after performing the following command
```python
python manage.py runserver
```

Task 8:
Create a Post class for modeling a post/article.
What are some of the things you want to capture
when writing an article,
Let me give you a bunch of parameters:
Determine what fields they should possess.
title - **
slug - **
author - **
body - **
publish - **
created - **
updated - **
status - **
also return a dunder string that can be a representative of
the model


Task 9:
create a super user
```python
python manage.py createsuperuser
```

Task 10:
create a post/article
```python
from django.contrib.auth.models import User
from blog.models import Post
user = User.objects.get(username='admin')
post = Post(
        title='Another post',
        slug='another-post',
        body='Post body.',
        author=user
)
post.save()
```

Task 10:
update the title of the post
```python
post.title = 'New title'
post.save()
```

Task 11:
retrieve all the posts that you have ever posted
```python
all_posts = Post.objects.all()
```

Task 12:
filter only the articles that were published in 2020 and were authored 
by the admin but exclude all the titles that starts with why and finally return them
arranged in descending order of their title heads

```python
Post.objects.filter(publish__year=2020,author__username='admin')
            .exclude(title__startswith='Why')
            .order_by('-title')
```


Task 13:
delete the second post that you had created
```python
posts = Post.objects.filter(author__username="winnie")
for index, post in enumerate(posts):
    if index == 1:
        post.delete()
```

Once completed push code and create a pull request so that I may be notified

Task 14:
create a model manager for managing published posts
```python
class PublishedManager(models.Manager):
 def get_queryset(self):
        return super(PublishedManager,
                self).get_queryset()\
                .filter(status='published')
```

Task 15:
Show all published posts on the web portal i.e in a html page
```python
from django.shortcuts import render, get_object_or_404
from .models import Post
def post_list(request):
 posts = Post.published.all()
 return render(request,
 'blog/post/list.html',
 {'posts': posts})
```