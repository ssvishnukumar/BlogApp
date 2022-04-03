from django.contrib import admin
from django.urls import include, path
from . import views

# from .views import Index
urlpatterns = [
    path('', views.index, name="home"),
]