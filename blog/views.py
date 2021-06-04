from django.views.generic import ListView, DetailView
from .models import Posts

class BlogListView(ListView):
    model = Posts
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Posts
    template_name = "post_detail.html"

