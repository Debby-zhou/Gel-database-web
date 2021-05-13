from django.shortcuts import render,HttpResponseRedirect,Http404,HttpResponse
from django.contrib import auth
import os
from .models import *


# Create your views here.
def logout(request):
    auth.logout(request)
    return render(request,'index.html')
def showhome(request):
    return render(request, 'home.html')
def showtemplate(request):
    return render(request, 'template.html')

