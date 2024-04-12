from django.urls import path
from .views import PostCreate

app_name = 'example_blog'

urlpatterns = [
    path('posts/new', PostCreate.as_view(), name='new_post'),
]
