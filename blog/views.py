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

def changeUsername(request):
    if request.method=="POST":
        User.email=request.POST.get("email")
        if form.is_valid():
            User.save()
            return redirect("../home")
    return render(request,"changeUsername.html",{})
def changePassword(request):
    return render(request,"changePassword.html",{})
def changeEmail(request):
    return render(request,"changeEmail.html",{})
def deleteAccount(request):
    return render(request,"deleteAccount.html",{})    