from django.urls import path
from .views import render_posts, post_detail

app_name= 'proyectos'

urlpatterns=[
    path("", render_posts, name="posts"),
    path("<int:post_id>/", post_detail, name="post_detail")
    ]