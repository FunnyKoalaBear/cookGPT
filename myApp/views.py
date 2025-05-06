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


def index(request):
    return render(request, "myApp/index.html")

