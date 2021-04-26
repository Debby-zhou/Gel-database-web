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

tissues = ['other','control','selfrenewal','mesoderm','mesendoderm','ectoderm','endoderm']
def showanalysis(request):
    tissue = [i.capitalize() for i in tissues]
    category_r = {}
    if 'category' in request.POST:
        category_r['result'] = request.POST.get('category')
    if request.method == 'POST':
        form = SelectGene(request.POST)
        for ele in tissue:
            if category_r['result'] == ele:
                formName = ele + 'gene'
                form = SelectGene(request.POST)[formName]
    else:
        form = SelectGene()['Controlgene']
    return render(request, 'analysis.html', {'form': form, 'c':category_r})

def select_result(request):  
    tissues_gene = [i.capitalize()+'gene' for i in tissues]
    gene_r = {}
    if request.method == 'POST':
        for ele,v in zip(tissues_gene,tissues):
            if ele in request.POST:
                form = SelectGene(request.POST)[ele]
                gene_r['result'] = request.POST[ele]
                fileName = "/static/assets/model/scorecard/ct_value_/" + v + "/interpolate/" + gene_r['result'] +".html"
        
    return render(request,"analysis.html",locals())

#* analysisdb
def showScorecardCT(request):
    try:
        form = SelectCategory()
        scorecardCT = ScorecardCtValues.User.objects.using('analysisdb').all()
    except:
        errormessage = "讀取錯誤！"
    return render(request, 'analysis.html', locals())
