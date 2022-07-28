from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):

    post = Post.objects.all()

    context = {
        "post" : post
    }

    return render(request,"home.html", context)

def about(request):
    return render(request,"about.html")