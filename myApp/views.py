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


@csrf_exempt
def updatePantry(request):

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            item = data.get("item")
            quantity = data.get("quantity")
            unit = data.get("unit")
            category = data.get("category")
        
            user = request.user

            # validating the category
            validCategories = {
                'vegies': 'veggies',
                'proteins': 'proteins',
                'carbs': 'carbs',
                'sauces': 'sauces',
                'special': 'special',
                'beverage': 'beverage',
            }

            if category not in validCategories:
                return JsonResponse({"error": "Invalid category"}, status=400)

            # getting/creating the ingredient
            item, created = Ingredient.objects.get_or_create(
                name=item,
                defaults={
                    "category": category,
                    "quantity": quantity,
                    "unit": unit
                }
            )

            if not created:
                if item.category != category:
                    item.category = category

                if item.unit != unit:
                    item.unit = unit
                
                item.quantity += quantity
                item.save()
            
            #create a pantry for the user 
            pantry, _ = Pantry.objects.get_or_create(user=user)

            #access category field 
            category_field = getattr(pantry, validCategories[category])

            #check if ingredient is already in pantry 
            if Ingredient not in category_field.all():
                category_field.add(Ingredient)
            else:
                Ingredient.quantity += quantity
                Ingredient.save()
            

            return JsonResponse({"status": 200})

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

    else:
        return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)


def meals(request):
    return render(request, "myApp/meals.html")


def saveRecipe(request):
    pass


def removeRecipe(request):
    pass

#hi from laptop 


