from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render,redirect
from app.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User  # To associate with Django's built-in User model
from django.db.models import Q
# Create your views here.
def home(request):
    con ={
    }
    return render (request, "index.html",con)
def about(request):
    con ={
    }
    return render (request, "about.html",con)
def contact(request):
    con ={
    }
    return render (request, "contact.html",con)
def project(request):
    con ={
    }
    return render (request, "project.html",con)
def team(request):
    con ={
    }
    return render (request, "team.html",con)
def service(request):
    con ={
    }
    return render (request, "service.html",con)
def testimonial(request):
    con ={
    }
    return render (request, "team.html",con)