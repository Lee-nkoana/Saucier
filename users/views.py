from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django import forms
# from .models import User

def index(request):
        return render(request, "users/index.html")


# Create your views here.
def login_view(request):
    if request.method == 'POST':

        #attempt to sign user in
        username  = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        #check if authentification is successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("profile"))
        else:
            return render(request, "users/login.html", {
                "message" : "Invalid username or password."
            })
    else:
        return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
      if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "users/register.html", {
                "message" : "Passwords must match."
            })
        
        #attemot to create a new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "users/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
      else:
        return render(request, "users/register.html")
      
@login_required
def profile(request):
    return render(request, "users/profile.html", {
        "user": request.user
    })