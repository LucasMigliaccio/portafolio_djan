from django.urls import path
from .views import Inicio, post_detail, render_posts

app_name= 'blog'

urlpatterns=[
    path("", render_posts, name="post"),
    path("<int:post_id>", post_detail, name="post_detail")
    ]