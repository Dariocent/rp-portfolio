from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("index_test", views.blog_index_test, name="blog_index_test"),

]
