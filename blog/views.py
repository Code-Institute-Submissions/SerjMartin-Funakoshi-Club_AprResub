from django.shortcuts import render, get_object_or_404
from django.views import generic, View
# Import Post model from models.py
from .models import Post


class PostList(generic.ListView):
    """
    Create Post List based on the generic list view model
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'


class PostDetail(View):
    """
    Create view to display post details
    """
    def get(self, request, slug, *args, **kwargs):
        quryset = Post.objects.filter(status=1)
        post = get_object_or_404(quryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
            },
        )
