from django.urls import path
from . import views

urlpatterns=[
    path("home/",views.home,name="home"),
    path("create/",views.create,name="create"),
    path("settings/",views.settings,name="settings"),
    path("",views.homepage,name="homepage"),
    path("signup/",views.signup,name="signup"),
    #logout
]