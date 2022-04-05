# From blog import views
from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('blog.html', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('edit_comment/<int:id>', views.edit_comment, name='edit_comment'),
    path(
        'delete_comment/<int:id>',
        views.delete_comment, name='delete_comment'),
]
