from django.shortcuts import render

def showtemplate1(request):
    return render(request, 'index.html') 
def showtemplate2(request):
    return render(request, 'register.html') 
def showtemplate3(request):
    return render(request, 'register_success.html') 
