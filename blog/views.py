from django.shortcuts import render,get_object_or_404
from django.views import generic

from blog.admin import PostAdmin
from .models import Post

# Create your views here.

from django.shortcuts import render, HttpResponse, get_object_or_404
from blog.models import Post
def post_list(request): #list
    post =Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': PostAdmin})

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    