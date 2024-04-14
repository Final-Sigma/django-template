from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .forms import PostForm
from .models import BlogPost as Post

class PostsIndex(ListView):
    model = Post
    paginate_by = 5

class PostsCreate(CreateView):
    # from FormMixin which FormView inherits.
    # initial = {}
    # form_class = None
    # success_url = None
    # prefix = None
    model = Post
    form_class = PostForm
    # template_name = 'example_blog/blogpost_form.html'

class PostsDetail(DetailView):
    model = Post

class PostsUpdate(UpdateView):
    model = Post
    form_class = PostForm

class PostsDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:posts')

def GeneralRedirect(pattern_name, permanent=False):
    return RedirectView.as_view(
        url=reverse_lazy(pattern_name),
        permanent=permanent
    )