from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
def index(request):
    return render(request, 'home.html')
#
#
# class Index(ListView):
#     template_name = 'home.html'
