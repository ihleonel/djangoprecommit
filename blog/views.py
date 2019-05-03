from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Blog


class IndexView(TemplateView):
    template_name = "index.html"


class ListBlogView(ListView):
    model = Blog
    template_name = "list_blog.html"
    context_object_name = "Blogs"


class CreateBlogView(CreateView):
    model = Blog
    template_name = "create_blog.html"
    success_url = reverse_lazy("list-blog")
    fields = ["titulo"]
