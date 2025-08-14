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

from .models import User, Ingredient, Pantry, MyRecipe

#cache control
from datetime import timedelta
from django.utils.cache import patch_cache_control

#ai api 
from openai import OpenAI

from dotenv import load_dotenv
import os
from openai import OpenAI

# Load .env file
load_dotenv()
api_key = os.getenv("api_key").strip()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1", 
  api_key=api_key
)

allCategories = ['vegies', 'proteins', 'carbs', 'sauces', 'special', 'beverage']

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
    

@login_required 
def designMeal(request):
    
    user = request.user
    
    #get/create the users pantry
    pantry, _ = Pantry.objects.get_or_create(user=user)

    #dictionary of all categories 
    pantryData = {}

    for field in allCategories:
        ingredients = getattr(pantry, field).all()

        #extracting ingredient information
        #makes arrays ina  dictionary
        #the arrays hold dictionaries of ingredients 
        pantryData[field] = [
            {
                "name": ing.name,
                "quantity": ing.quantity,
                "unit": ing.unit_of_measurement,
                "category": ing.category
            }
            for ing in ingredients
        ]

    return render(request, "myApp/designMeal.html", {"pantry": pantryData})


@login_required 
def generateRecipe(request):
    if request.method == "POST":
        
        try:
            data = json.loads(request.body)
            ingredients = data.get("ingredients")
            query = data.get("query")

            print("DEBUG: API key =", os.getenv("api_key"))
            print("DEBUG: Ingredients =", ingredients)
            print("DEBUG: Query =", query)

            completion = client.chat.completions.create(
                extra_body={},
                model="gpt-3.5-turbo",  
                messages=[
                    {
                    "role": "user",
                    "content": f"{query}, with the ingredients: {ingredients}, include recipe title in the first line."
                    }
                ]
            )

            query = f"{query}, with the ingredients: {ingredients}, give recipe for 1 serving only"
            message = completion.choices[0].message.content
            recipeTitle = message.split("\n")[0]
            message = "\n".join(message.split("\n")[2:])
            

            print(recipeTitle)
            print(query)
            print(message)
            
            return JsonResponse({"status": 200, "message": message, "recipeTitle": recipeTitle}, status=200)
            
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)




@login_required 
def pantry(request):
    user = request.user

    #get/create the users pantry
    pantry, _ = Pantry.objects.get_or_create(user=user)

    #dictionary of all categories 
    pantryData = {}

    for field in allCategories:
        ingredients = getattr(pantry, field).all()

        #extracting ingredient information
        #makes arrays ina  dictionary
        #the arrays hold dictionaries of ingredients 
        pantryData[field] = [
            {
                "name": ing.name,
                "quantity": ing.quantity,
                "unit": ing.unit_of_measurement,
                "category": ing.category
            }
            for ing in ingredients
        ]
        


    return render(request, "myApp/pantry.html", {"pantry": pantryData})


@csrf_exempt
@login_required 
def updatePantry(request):

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            item = data.get("item")
            quantity = float(data.get("quantity", 0))
            unit = data.get("unit")
            category = data.get("category", "").strip()
            
    
            user = request.user
            
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

            #create a pantry for the user 
            pantry, _ = Pantry.objects.get_or_create(user=user)

            #access correct manyToMany field 
            category_field = getattr(pantry, category_field_mapping[category])


            # getting/creating the ingredient
            item, created = Ingredient.objects.get_or_create(
                name=item,
                defaults={
                    "category": category,
                    "quantity": 0, #add quantity later 
                    "unit_of_measurement": unit
                }
            )  
            
            item.category = category
            item.unit_of_measurement = unit
            item.quantity += quantity
            item.save()
            
            #check if ingredient is already in pantry 
            if item not in category_field.all():
                category_field.add(item)
            
            return JsonResponse({"status": 200})
            
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

        

@login_required 
def updateIngredient(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            item = data.get("item")
            action = data.get("action")    
            user = request.user
            
            ingredient = Ingredient.objects.get(name=item, user=user)
            
            if action == "increment":
                ingredient.quantity += 1

            elif action == "decrement":
                ingredient.quantity -=1

            elif action == "trash":
                ingredient.delete()
                return JsonResponse({"status": 200, "message": f"{item} deleted"})
            
            ingredient.save()
            return JsonResponse({"status": 200, "message": f"{item} updated"})
        
        except Ingredient.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Ingredient not found"}, status=404)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)




@login_required 
def meals(request):
    user = request.user
    recipes = MyRecipe.objects.filter(user=user)


    return render(request, "myApp/meals.html", {
        "recipes": recipes
    })


@login_required 
def saveRecipe(request):

    if request.method == "POST":
        
        try:
            data = json.loads(request.body)
            recipeTitle = data.get("recipeTitle")
            recipe = data.get("recipe")

            print("DEBUG RECIPE TITLE: ", recipeTitle)
            print("DEBUG RECIPE INSTRUCTION: ", recipe)

            #saving the recipe
            myRecipe = MyRecipe.objects.create(
                user = request.user,
                recipeTitle = recipeTitle,
                recipe = recipe
            )
            
            return JsonResponse({"status": "success", "Recipe Title": myRecipe.recipeTitle})
        
        except Exception as e: 
            return JsonResponse({"status": "error", "message": str(e)}, status=400)



@login_required 
def removeRecipe(request):
    pass

#hi from my laptop 

