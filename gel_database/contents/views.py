from django.shortcuts import render,HttpResponseRedirect,Http404,HttpResponse
from contents.models import E200317Score,E201016Score,E200317Parameter,E201016Parameter,E200317CtValues,E200317FoldChange
import pymysql as pysql
from contents.forms import SelectDataForm
# Create your views here.
def showhome(request):
    return render(request, 'home.html')
def showexperiment(request):
    return render(request, 'experiment.html')
def showsimulation(request):
    return render(request, 'simulation.html')
def showanalysis(request):
    return render(request, 'analysis.html')
def showtemplate(request):
    return render(request, 'template.html')
def showiframe(request):
    return render(request, 'scorecard/ct_value_/control/interpolate/ACTB.1.html')

def score200317(request):
    try:
        form = SelectDataForm()
        score200317 = E200317Score.objects.all()
    except:
        errormessage = "讀取錯誤！"
    return render(request, 'experiment.html', locals())    
def score201016(request):
    try:
        form = SelectDataForm()
        score201016 = E201016Score.objects.all()
    except:
        errormessage = "讀取錯誤！"  
    return render(request, 'experiment.html', locals())
def parameter200317(request):
    try:
        form = SelectDataForm()
        parameter200317 = E200317Parameter.objects.all()
    except:
        errormessage = "讀取錯誤！"  
    return render(request, 'experiment.html', locals())
def parameter201016(request):
    try:
        form = SelectDataForm()
        parameter201016 = E201016Parameter.objects.all()
    except:
        errormessage = "讀取錯誤！"  
    return render(request, 'experiment.html', locals())
def ctvalues200317(request):
    try:
        form = SelectDataForm()
        ctvalues200317 = E200317CtValues.objects.all()
    except:
        errormessage = "讀取錯誤！"     
    return render(request, 'experiment.html', locals())
def foldchanges200317(request):
    try:
        form = SelectDataForm()
        foldchanges200317 = E200317FoldChange.objects.all()
    except:
        errormessage = "讀取錯誤！"    
    return render(request, 'experiment.html', locals())

def select_data(request):
    if request.method == 'POST':
        form = SelectDataForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('score200317/#result')
    else:
        form = SelectDataForm()
    return render(request,'experiment.html', {'form': form})
