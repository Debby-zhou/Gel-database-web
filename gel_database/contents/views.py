from django.shortcuts import render,HttpResponseRedirect,Http404,HttpResponse
from django.contrib import auth
import os
from contents.forms import SelectData, SelectGene
from .models import *
from django.forms.models import model_to_dict

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
    models = [CtValueControl,CtValueEctoderm,CtValueEndoderm,CtValueMesendoderm,CtValueMesoderm,CtValueOther,CtValueSelfrenewal,FoldChangeEctoderm,FoldChangeEndoderm,FoldChangeMesendoderm,FoldChangeMesoderm,FoldChangeSelfrenewal]
    if request.POST:
        final = {}
        for ele,key in zip(keys,ori_keys):
                exp_r[ele] = request.POST.get(key)
        if 'parameter' in exp_r.values():
                fields = get_model_field(MechanicalParameter)
                result = get_model_data(MechanicalParameter)
        elif 'score' in exp_r.values():
                fields = get_model_field(Score)
                result = get_model_data(Score)
        else: 
            r = "<class 'contents.models." + exp_r['expression'] + exp_r['tissue'] + "'>"
            for ele in models:
                if r == str(ele):
                    tableExist = True
                    fields = get_model_field(ele)
                    fields = fields[8:]
                    result = get_model_data(ele)
                    break
        a = 0
        for r in result:
            final[a] = model_to_dict(r)
            a += 1
    return render(request,'result.html',locals())
def get_model_field(modelName):
    fields = [f.name for f in modelName._meta.get_fields()]
    return fields
def get_model_data(modelName):
    try:
        result = modelName.objects.all()
    except:
        result = "Import error!"
    return result

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
