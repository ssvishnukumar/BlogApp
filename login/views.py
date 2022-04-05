from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy # for redirecting back
from django.contrib.auth.forms import User
class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    # UserCreationForm - uses django inbuilt User model to process the user.
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    # after the success_url it will be redirected to the login page.
