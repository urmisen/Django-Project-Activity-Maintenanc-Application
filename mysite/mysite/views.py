from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'project/index.html', {'title': 'home'})

def about(request):
    return render(request, 'project/about.html', {'title': 'about'})

def contact(request):
    return render(request, 'project/contact.html', {'title': 'contact'})

def service(request):
    return render(request, 'project/service.html', {'title': 'service'})

