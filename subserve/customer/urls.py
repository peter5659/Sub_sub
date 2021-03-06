from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('signin/', views.signIn, name="signin"),
    path('signup/', views.signUp, name="signup"),
    path('confirmpassword', views.confirmPassword, name="confirmpassword"),
    path('editprofile/', views.editProfile, name="editprofile"),
    path('findaccount/', views.findAccount, name="findaccount"),
    path('mypage/', views.myPage, name="mypage"),
    path('resign/', views.resign, name="resign")
]
