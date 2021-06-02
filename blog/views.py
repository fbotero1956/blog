from django.views.generic import ListView
from .models import Posts

class BlogListView(ListView):
    model = Posts
    template_name = "home.html"



