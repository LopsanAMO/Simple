from django.shortcuts import render
from django.views.generic import View


def home(request):
    if request.method == 'GET':
        template_name = 'index.html'
        return render(request, template_name)

def login(request):
    if request.method == 'GET':
        template_name = 'login.html'
        return render(request, template_name)
