from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login_view", views.login_view, name="login_view"),
    path("register", views.register, name="register"),
    path("logout_view", views.logout_view, name="logout_view"),    
    path("designMeal", views.designMeal, name="designMeal"),
    path("pantry", views.pantry, name="pantry"),
    path("meals", views.meals, name="meals"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)