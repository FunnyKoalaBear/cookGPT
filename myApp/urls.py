from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login_view", views.login_view, name="login_view"),
    path("register", views.register, name="register"),
    path("logout_view", views.logout_view, name="logout_view"),    
    path("designMeal", views.designMeal, name="designMeal"),
    path("pantry", views.pantry, name="pantry"),
    path('myApp/updatePantry/', views.updatePantry, name='updatePantry'),
    path('myApp/updateIngredient/', views.updateIngredient, name='updateIngredient'),
    path('myApp/generateRecipe/', views.generateRecipe, name='generateRecipe'),
    path("meals", views.meals, name="meals"),
    path('admin/', admin.site.urls),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)