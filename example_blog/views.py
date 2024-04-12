from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView
from .forms import PostForm
from .models import BlogPost as Post

class PostCreate(CreateView):
    # from FormMixin which FormView inherits.
    # initial = {}
    # form_class = None
    # success_url = None
    # prefix = None
    model = Post
    form_class = PostForm
    # template_name = 'example_blog/blogpost_form.html'
