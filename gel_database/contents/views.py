from django.shortcuts import render,HttpResponseRedirect,Http404,HttpResponse
from django.contrib import auth
import os
from contents.forms import SelectData, SelectGene
from .models import *

# Create your views here.
def logout(request):
    auth.logout(request)
    return render(request,'logout.html')
def showhome(request):
    return render(request, 'home.html')
def showsimulation(request):
    return render(request, 'simulation.html')
def showtemplate(request):
    return render(request, 'template.html')
def showexperiment(request):
    if request.method == "POST":
        form = SelectData(request.POST)
        if form.is_valid:
            return HttpResponseRedirect("../experiment")
    else:
        form = SelectData()
    return render(request,'experiment.html', locals())
def show_experiment_result(request):
    exp_r = {}
    keys = ['mechanical','expression','tissue']
    ori_keys = ['mechanical','cell_diff_expression','cell_diff_tissue']    
    tissues = ['Control','Ectoderm','Endoderm','Mesendoderm','Mesoderm','Other','Selfrenewal'] 
    if request.POST:
        for ele,key in zip(keys,ori_keys):
            if ele == 'tissue':
                exp_r[ele] = request.POST.getlist(key)
            else:
                exp_r[ele] = request.POST.get(key)
    for i,j in exp_r.items():
        if i == 'mechanical':
            resultTable = getdata('MechanicalParameter')
    return render(request,'result.html',locals())
def getdata(modelName):
    try:
        t = modelName.objects.all()
    except:
        t = "Import error！"
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
