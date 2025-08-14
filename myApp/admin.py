from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Ingredient, Pantry, MyRecipe

# Custom User admin
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "is_staff", "is_superuser")
    search_fields = ("username", "email")
    ordering = ("username",)

# Ingredient admin
@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "quantity", "unit_of_measurement", "user")
    list_filter = ("category", "unit_of_measurement")
    search_fields = ("name",)

# Pantry admin
@admin.register(Pantry)
class PantryAdmin(admin.ModelAdmin):
    list_display = ("user",)
    filter_horizontal = ("vegies", "proteins", "carbs", "sauces", "special", "beverage")

# MyRecipe admin
@admin.register(MyRecipe)
class MyRecipeAdmin(admin.ModelAdmin):
    list_display = ("recipeTitle", "user")
    search_fields = ("recipeTitle", "user__username")
