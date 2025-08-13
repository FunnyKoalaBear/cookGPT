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
@login_required 
def updatePantry(request):

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            item = data.get("item")
            quantity = float(data.get("quantity", 0))
            unit = data.get("unit")
            category = data.get("category")
        
            user = request.user

            # validating the category
            validCategories = {
                'vegies': 'Veggies & Fruits',
                'proteins': 'Proteins',
                'carbs': 'Carbs',
                'sauces': 'Sauces & Spices',
                'special': 'Special',
                'beverage': 'Beverages',
            }

            
            category_field_mapping = {
                'Veggies & Fruits': 'vegies',
                'Proteins': 'proteins',
                'Carbs': 'carbs',
                'Sauces & Spices': 'sauces',
                'Special': 'special',
                'Beverages': 'beverage',
            }

            if category not in category_field_mapping:
                return JsonResponse({"status": "error", "message": f"Invalid category: {category}"}, status=400)

            category_field = getattr(pantry, category_field_mapping[category])

            # getting/creating the ingredient
            item, created = Ingredient.objects.get_or_create(
                name=item,
                defaults={
                    "category": category,
                    "quantity": quantity,
                    "unit_of_measurement": unit
                }
            )

            if not created:
                if item.category != category:
                    item.category = category

                if item.unit_of_measurement != unit:
                    item.unit_of_measurement = unit

                item.quantity += quantity
                item.save()
            
            #create a pantry for the user 
            pantry, _ = Pantry.objects.get_or_create(user=user)

            
            #access category field 
            category_field = getattr(pantry, validCategories[category])

            #check if ingredient is already in pantry 
            if item not in category_field.all():
                category_field.add(item)
            else:
                existing_item = category_field.get(pk=item.pk)
                existing_item.quantity += quantity
                existing_item.save()
            
            return JsonResponse({"status": 200})
            
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

        

def meals(request):
    return render(request, "myApp/meals.html")


def saveRecipe(request):
    pass


def removeRecipe(request):
    pass

#hi from laptop 


