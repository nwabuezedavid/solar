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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        service = request.POST['service']
        special_note = request.POST['special_note']

        # Save data to the database
        ContactForm.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            service=service,
            special_note=special_note
        )
        messages.info(request,'sent , you will be contacted soon')
        return redirect('home')
    con ={
        "site":siteedit.objects.get(idx = 1),
        "team_members" : expertteam.objects.order_by('id') 
        
    }
    return render (request, "index.html",con)
def about(request):
    con ={
        "site":siteedit.objects.get(idx = 1),
        "team_members" : expertteam.objects.order_by('id') 
        
    }
    return render (request, "about.html",con)
def contact(request):
    con ={
        "site":siteedit.objects.get(idx = 1)
    }
    return render (request, "contact.html",con)
def project(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        service = request.POST['service']
        special_note = request.POST['special_note']

        # Save data to the database
        ContactForm.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            service=service,
            special_note=special_note
        )
        messages.info(request,'sent , you will be contacted soon')
        return redirect('project')
    con ={
        "site":siteedit.objects.get(idx = 1)
    }
    return render (request, "project.html",con)
def team(request):
    con ={
        "site":siteedit.objects.get(idx = 1),
        "team_members" : expertteam.objects.order_by('id') 
    }
    return render (request, "team.html",con)
def service(request):
    con ={
        "site":siteedit.objects.get(idx = 1)
    }
    return render (request, "service.html",con)
def testimonial(request):
    con ={
        "site":siteedit.objects.get(idx = 1)
    }
    return render (request, "testimonial.html",con)
def quote(request):
    con ={
        "site":siteedit.objects.get(idx = 1)
    }
    return render (request, "quote.html",con)
def Policy(request):
    con ={
        "site":siteedit.objects.get(idx = 1)
    }
    return render (request, "poilcy.html",con)