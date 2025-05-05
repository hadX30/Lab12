from django.contrib import admin
from django.urls import path
from . import views
from .views import register, CustomLoginView



urlpatterns = [
    path('register/',register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path("logout/", views.logoutUser, name="logout")
]
