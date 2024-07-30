from django.urls import path
from . import views

urlpatterns=[
    path("home/",views.home,name="home"),
    path("create/",views.create,name="create"),
    path("settings/",views.settings,name="settings"),
    path("",views.homepage,name="homepage"),
    path("signup/",views.signup,name="signup"),
    path("changeUsername/",views.changeUsername,name="changeUsername"),
    path("changePassword/",views.changePassword,name="changePassword"),
    path("changeEmail/",views.changeEmail,name="changeEmail"),
    path("deleteAccount/",views.deleteAccount,name="deleteAccount"),
]