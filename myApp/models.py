from django.contrib.auth.models import AbstractUser
from django.db import models 

#gives field types like CharField, IntegerField, TextField, ImageField
#relatoinships like OneToOneField, ForeignKey, ManyToManyField


class User(AbstractUser):
    def __str__(self):
        return f"{self.username}, ({self.email})"



class Ingredient(models.Model):
    
    CATEGORY_CHOICES = [
        ('vegies', 'Vegies'), #(whats stored, whats shown)
        ('proteins', 'Proteins'),
        ('carbs', 'Carbs'),
        ('sauces', 'Sauces'),
        ('special', 'Special'),
        ('beverage', 'Beverage')
    ]

    UNITS = [
        ('g', 'grams'),
        ('kg', 'kilograms'),
        ('ml', 'milliliters'),
        ('l', 'liters'),
        ('tsp', 'teaspoons'),
        ('tbsp', 'tablespoons'),
        ('cup', 'cups'),
        ('piece', 'pieces'),
        ('slice', 'slices'),
    ]

    def clean(self):
        if self.quantity is not None and self.quantity < 0:
            self.quantity = 1
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    quantity = models.FloatField(default=1) 
    unit_of_measurement = models.CharField(max_length=20, choices=UNITS, default='piece')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='unique_ingredient_per_user')
        ]

    def __str__(self):
        return f"{self.name} ({self.user.username})"



class Pantry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pantry")
    vegies = models.ManyToManyField(Ingredient, related_name="vegies", blank=True)
    proteins = models.ManyToManyField(Ingredient, related_name="proteins", blank=True)
    carbs = models.ManyToManyField(Ingredient, related_name="carbs", blank=True)
    sauces = models.ManyToManyField(Ingredient, related_name="sauces", blank=True)
    special = models.ManyToManyField(Ingredient, related_name="special", blank=True)
    beverage = models.ManyToManyField(Ingredient, related_name="beverage", blank=True)

    def __str__(self):
        return f"{self.user.username}'s pantry"



class MyRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe")
    recipeName = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient, blank=True)

    def __str__(self):
        return f"{self.recipeName} by {self.user.username}"



class InstructionStep(models.Model):
    recipe = models.ForeignKey(MyRecipe, on_delete=models.CASCADE, related_name="steps")
    step_number = models.PositiveIntegerField()
    description = models.TextField()

    class Meta:
        ordering = ["step_number"]

    def __str__(self):
        return f"Step {self.step_number}: {self.description[:30]}..."
    
