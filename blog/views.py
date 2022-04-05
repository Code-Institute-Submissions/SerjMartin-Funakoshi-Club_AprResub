from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Import Post model from models.py
from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    """
    Create Post List based on the generic list view model
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'


class PostDetail(View):
    """
    Create view to display post details .filter(approved=True).filter(status=1)
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
                # "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        quryset = Post.objects.filter(status=1)
        post = get_object_or_404(quryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment_form.save()
            messages.success(request, 'Your comment is successfully submited.')
        else:

            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                # "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


class PostLike(View):
    """
    Create method view to display likes
    """

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def edit_comment(request, id):
    """ Edit an existing Post """

    comment = get_object_or_404(Comment, pk=id)
    if comment.name != request.user.username:
        messages.error(request, "You can't edit this post")
        return redirect('blog')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.instance.body = request.POST.get('body')
            comment_form.save()
            messages.success(request, 'Successfully updated comment!')
            return redirect(reverse('post_detail', args=[comment.post.slug]))
        else:
            messages.error(
                request, 'Failed to update comment. check if form is valid.')
    else:
        comment_form = CommentForm(instance=comment)
        print(comment_form)
        messages.info(request, 'You are editing this comment')
    template = 'edit.html'
    context = {
        # 'post': post,
        'comment_form': comment_form,
    }

    return render(request, template, context)


@login_required
def delete_comment(request, id):
    """ Create method view to display likes """

    comment = get_object_or_404(Comment, pk=id)
    if comment.name != request.user.username:
        messages.error(request, "You can't delete this post")
        return redirect('blog')

    comment.delete()
    messages.success(request, 'Comment deleted')

    return redirect(reverse('post_detail', args=[comment.post.slug]))
