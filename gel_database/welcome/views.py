from django.shortcuts import render

def showindex(request):
    return render(request, 'index.html') 
def showregister(request):
    return render(request, 'register.html') 
def showregistersuccess(request):
    return render(request, 'register_success.html') 
