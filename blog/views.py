from django.shortcuts import render
from django.views import generic
# Import Post model from models.py
from .models import Post


class PostList(generic.ListView):
    """
    Create Post List based on the generic list view model
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
