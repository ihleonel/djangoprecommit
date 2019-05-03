from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("blog/list", views.ListBlogView.as_view(), name="list-blog"),
    path("blog/create", views.CreateBlogView.as_view(), name="create-blog"),
]
