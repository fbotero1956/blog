from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, 
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from .models import Posts


class BlogListView(ListView):
    model = Posts
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Posts
    template_name = "post_detail.html"

class BlogCreateView(CreateView):
    model = Posts
    template_name = "post_new.html"
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Posts
    template_name = "post_edit.html"
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Posts
    template_name = "post_delete.html"
    success_url = reverse_lazy('home')