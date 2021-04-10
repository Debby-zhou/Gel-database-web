from django.shortcuts import render,HttpResponseRedirect,Http404,HttpResponse
from django.template import RequestContext
from welcome.forms import UserRegister, UserLogin
from welcome.models import User
from django.contrib import auth

def showindex(request):
    form = UserLogin(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/contents')
        else:
            errormsg = "Username or password is wrong, please log in again!"
    return render(request, 'index.html', locals())
def showregister(request):
    form = UserRegister(request.POST)
    return render(request,'register.html', locals())
def showsuccess(request):
    return render(request, 'success.html') 
  

