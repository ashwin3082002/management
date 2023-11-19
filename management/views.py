from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    messages.info(request, "Hello world!")
    
    return render(request, 'index.html')