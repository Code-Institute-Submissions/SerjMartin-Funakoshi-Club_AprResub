from django.db import models

# Import the user model from django
from django.contrib.auth.models import User

# Import cloudinary field for the future images
from cloudinary.models import CloudinaryField

# Ceate a tuple for the status (0 as draft) and (1 as published)
STATUS = ((0, "Draft"), (1, "Published"))

# Convert database table into Django models
# Add Post model


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    # Return a string representation
    def __str__(self):
        return self.title

    # Return total number of likes
    def number_of_likes(self):
        return self.likes.count()


# Add Comment model

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)

    class Meta:
        ordering = ['created_on']

    # Return string comments and author
    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def number_of_likes(self):
        return self.likes.count()
