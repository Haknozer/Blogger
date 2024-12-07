from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("blogs",views.blog_add,name="blog_add"),
    path("blog/<slug:slug>",views.blog_details,name="blog_details"),

]
