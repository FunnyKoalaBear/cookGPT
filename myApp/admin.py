from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Ingredient, Pantry, MyRecipe, InstructionStep

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
    list_display = ("recipeName", "user")
    search_fields = ("recipeName", "user__username")
    filter_horizontal = ("ingredients",)

# InstructionStep admin
@admin.register(InstructionStep)
class InstructionStepAdmin(admin.ModelAdmin):
    list_display = ("recipe", "step_number", "description_short")
    list_filter = ("recipe",)

    def description_short(self, obj):
        return obj.description[:50] + "..." if len(obj.description) > 50 else obj.description
    description_short.short_description = "Description"
