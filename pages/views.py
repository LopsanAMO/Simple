from django.shortcuts import render
from django.views.generic import View


def home_bancomer(request):
    if request.method == 'GET':
        template_name = 'index.html'
        return render(request, template_name)

def login_bancomer(request):
    if request.method == 'GET':
        template_name = 'login.html'
        return render(request, template_name)

def escoti_click(request):
    if request.method == 'GET':
        template_name = 'click.html'
        return render(request, template_name)

def table_escoti(request):
    if request.method == 'GET':
        template_name = 'table.html'
        return render(request, template_name)
