from django.shortcuts import render,HttpResponseRedirect,Http404,HttpResponse
from contents.models import E200317Score,E201016Score,E200317Parameter,E201016Parameter,E200317CtValues,E200317FoldChange,ScorecardCtValues
'''
from contents.models_a import E1227SimulationResult,E201016CtValuesControl,E201016CtValuesMesendoderm,E201016CtValuesMesoderm,E201016CtValuesSelfrenewal,E201016DctValueEctoderm,E201016DctValueEndoderm,E201016DctValueOther,E201016FoldChangeEctoderm,E201016FoldChangeEndoderm,E201016FoldChangeMesendoderm,E201016FoldChangeMesoderm,E201016FoldChangeSelfrenewal,ScorecardCtValues
import pymysql as pysql
'''
import os
from contents.forms import SelectDataForm, SelectGene
# Create your views here.
def showhome(request):
    return render(request, 'home.html')
def showsimulation(request):
    return render(request, 'simulation.html')
def showtemplate(request):
    return render(request, 'template.html')
def showexperiment(request):
    if request.method == 'POST':
        form = SelectDataForm(request.POST)
        if form.is_valid:
            return HttpResponseRedirect("../experiment")
    else:
        form = SelectDataForm()
    return render(request,'experiment.html', {'form': form})
def show_experiment_result(request):
    exp_r = {}
    form = SelectDataForm()
    if request.method == 'POST':
        form = SelectDataForm(request.POST)        
        if request.POST:
            exp_r['time'] = request.POST['time']
            exp_r['type'] = request.POST['table']
            if exp_r['time']=='200317':
                if exp_r['type']=='score':
                    score200317 = getdata(E200317Score)
                elif exp_r['type']=='parameter':
                    parameter200317 = getdata(E200317Parameter)
                elif exp_r['type']=='ctvalues':
                    ctvalues200317 = getdata(E200317CtValues)
                elif exp_r['type']=='foldchanges':
                    foldchanges200317 = getdata(E200317FoldChange)
            elif exp_r['time']=='201016':
                if exp_r['type']=='score':
                    score201016 = getdata(E201016Score)   
                elif exp_r['type']=='parameter':
                    parameter201016 = getdata(E201016Parameter)  
                elif exp_r['type']=='ctvalues':
                    ctvalues201016 = getdata(E201016CtValues)   
    return render(request,'experiment.html',locals())
def getdata(modelName):
    try:
        t = modelName.objects.all()
    except:
        t = "讀取錯誤！"
    return t
def showanalysis(request):
    category_r = {}
    if 'category' in request.POST:
        category_r['result'] = request.POST.get('category')
    if request.method == 'POST':
        form = SelectGene(request.POST)
        # if form.is_valid():
        #     return HttpResponseRedirect('../analysis')
        if category_r['result'] == 'Other':
            form = form['othergene']
        elif category_r['result'] == 'Control':
            form = form['controlgene']
        elif category_r['result'] == 'Self-renewal':
            form = form['selfrenewalgene']
        elif category_r['result'] == 'Mesoderm':
            form = form['mesodermgene']
        elif category_r['result'] == 'Mesendoderm':
            form = form['mesendodermgene']
        elif category_r['result'] == 'Ectoderm':
            form = form['ectodermgene'] 
        elif category_r['result'] == 'Endoderm':
            form = form['endodermgene'] 
    else:
        form = SelectGene(request.POST)
        form = form['controlgene']
    return render(request, 'analysis.html', {'form': form, 'c':category_r})
def select_result(request):   
    gene_r = {}
    form = SelectGene()
    if request.method == 'POST':
        form = SelectGene(request.POST)
        if form.is_valid():
             return HttpResponseRedirect('/contents/analysis')
    form = form['controlgene']
    if 'controlgene' in request.POST:
        gene_r['result'] = request.POST['controlgene']
        fileName = "/static/scorecard/ct_value_/control/interpolate/" + gene_r['result'] +".html"
    elif 'othergene' in request.POST:
        gene_r['result'] = request.POST['othergene']
        fileName = "/static/scorecard/ct_value_/other/interpolate/" + gene_r['result'] +".html"
    elif 'selfrenewalgene' in request.POST:
        gene_r['result'] = request.POST['selfrenewalgene']
        fileName = "/static/scorecard/ct_value_/selfrenewal/interpolate/" + gene_r['result'] +".html"
    elif 'ectodermgene' in request.POST:
        gene_r['result'] = request.POST['ectodermgene']
        fileName = "/static/scorecard/ct_value_/ectoderm/interpolate/" + gene_r['result'] +".html"
    elif 'endodermgene' in request.POST:
        gene_r['result'] = request.POST['endodermgene']
        fileName = "/static/scorecard/ct_value_/endoderm/interpolate/" + gene_r['result'] +".html"
    elif 'mesodermgene' in request.POST:
        gene_r['result'] = request.POST['mesodermgene']
        fileName = "/static/scorecard/ct_value_/mesoderm/interpolate/" + gene_r['result'] +".html"
    elif 'mesendodermgene' in request.POST:
        gene_r['result'] = request.POST['mesendodermgene']
        fileName = "/static/scorecard/ct_value_/mesendoderm/interpolate/" + gene_r['result'] +".html"
    return render(request,"analysis.html",locals())

#* analysisdb
def showScorecardCT(request):
    try:
        form = SelectCategory()
        scorecardCT = ScorecardCtValues.User.objects.using('analysisdb').all()
    except:
        errormessage = "讀取錯誤！"
    return render(request, 'analysis.html', locals())
