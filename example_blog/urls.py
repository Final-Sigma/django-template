from django.urls import path
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from .models import BlogPost
from .views import PostsIndex, PostsCreate, PostsDetail, PostsUpdate, PostsDelete, GeneralRedirect

app_name = 'example_blog'

urlpatterns = [
    path('', GeneralRedirect('blog:posts')),

    path('posts/',            PostsIndex.as_view(),  name='posts'),
    path('posts/new',         PostsCreate.as_view(), name='new_post'),
    path('posts/<pk>/',       PostsDetail.as_view(), name='post'),
    path('posts/<pk>/edit',   PostsUpdate.as_view(), name='edit_post'),
    path('posts/<pk>/delete', PostsDelete.as_view(), name='delete_post'),
]
