from django.shortcuts import render,redirect
from .models import userData
from . import forms

def home(request):
    data=userData.objects.all()
    blogs=list()
    for x in reversed(data):
        blogs.append(x.blog)
    return render(request,"home.html",{"blogs":blogs})

def create(request):
    if request.method=="POST":
        blogPost=request.POST.get("blogPost")
        newBlog=userData()
        newBlog.blog=blogPost
        newBlog.save()
    return render(request,"create.html",{})

def settings(request):
    return render(request,"settings.html",{})

def homepage(request):
    return render(request,"homepage.html",{})

def signup(request):
    if request.method=="POST":
        form=forms.signupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("../../")
    else:
        form=forms.signupForm()
    return render(request,"signup.html",{"form":form})

