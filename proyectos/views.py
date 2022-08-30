from django.shortcuts import render, get_object_or_404
from .models import Posts

# Create your views here.



def render_posts(request):
    post= Posts.objects.all()
    return render(request, 'post_proy.html',{"posts":post})

def post_detail(request, post_id):
    posts=get_object_or_404(Posts, pk=post_id)
    return render(request, "post_detail_proy.html", {"post":posts})