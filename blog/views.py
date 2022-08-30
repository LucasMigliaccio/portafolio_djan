from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from blog.models import Post
import random
#from .models import Posts
# Create your views here.

class Inicio(ListView):
    def get(self,request,*args, **kwargs):
        posts= list(Post.objects.filter(
            estado= True, 
            publicado= True
            ).values_list("id", flat=True)) #para obtenerlos sin hacerlos tupla
        
        #print("++++++++++++++++++++",posts)
        principal= random.choice(posts)

        principal= Post.objects.get(id= principal)
        

        return render(request, "indexpost.html",{"principal":principal})


def render_posts(request):
    post= Post.objects.all()
    return render(request, 'post.html',{"posts":post})

def post_detail(request, post_id):
    posts=get_object_or_404(Post, pk=post_id)
    return render(request, "post_detail.html", {"post":posts})

