from django.shortcuts import render
from django.template import RequestContext
from welcome.forms import UserRegister, UserLogin
from welcome.models import User
import hashlib

def showindex(request):
    return render(request, 'index.html') 
def showregister(request):
    return render(request, 'register.html') 
def showsuccess(request):
    return render(request, 'success.html') 

def take_md5(content):
    hash = hashlib.md5()    #建立hash加密例項
    hash.update(content)    #hash加密
    result = hash.hexdigest()  #得到加密結果
    return result

def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid(): 
            username = form.cleaned_data['username']
            namefilter = Register.objects.filter(username = username)
            if len(namefilter) > 0:
                return render(request,'register.html',{'error':'This username has already existed.'},context_instance=RequestContext(request))
            else:
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                if password1 != password2:
                    return render(request,'register.html',{'error':'Two sets of password input are inconsistent.'},context_instance=RequestContext(request))
                else:
                    password = take_md5(password1)
                    email = form.cleaned_data['email']
                    user = Register.objects.create(username=username,password=password,email=email )
                    user.save()
                    return render(request,'success.html',{'username':username,'operation':'Register'}, context_instance=RequestContext(request))
    else:
        form = UserRegister()
        return render(request,'register.html',{'form':form},context_instance=RequestContext(request))

def login(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid(): 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password = take_md5(password)
            namefilter = Register.objects.filter(username=username,password=password)
            if len(namefilter) > 0:
                return render(request,'success.html',{'username':username,'operation':'Login'},context_instance=RequestContext(request))
            else:
                return render(request,'index.html',{'error':'This username does not exist!'},context_instance=RequestContext(request))
        else:
            form = UserLogin()
            return render(request,'index.html',{'form':form}, context_instance=RequestContext(request))
