from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.shortcuts import render, redirect  
from django.contrib import messages

from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import login_required

from .models import User, Ingredient, Pantry, MyRecipe, InstructionStep

#cache control
from datetime import timedelta
from django.utils.cache import patch_cache_control



def index(request):
    response = render(request, 'myApp/index.html')
    # Set Cache-Control header to cache for 1 day
    patch_cache_control(response, max_age=86400)  # 86400 seconds = 1 day
    return response


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "myApp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "myApp/login.html")


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
            return render(request, "myApp/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "myApp/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "myApp/register.html")
    

def designMeal(request):
    return render(request, "myApp/designMeal.html")


def makeRecipe(request):
    pass


def pantry(request):
    return render(request, "myApp/pantry.html")


def meals(request):
    return render(request, "myApp/meals.html")


def saveRecipe(request):
    pass


def removeRecipe(request):
    pass

#hi from laptop 


