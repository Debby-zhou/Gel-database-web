from django.shortcuts import render,HttpResponseRedirect,Http404,HttpResponse
from django.contrib import auth
import os
from experiment.forms import SelectData, UploadExpData
from .models import *
from django.forms.models import model_to_dict
import csv

def logout(request):
    auth.logout(request)
    return render(request,'index.html')
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
            r = "<class 'experiment.models." + exp_r['expression'] + exp_r['tissue'] + "'>"
            for ele in models:
                if r == str(ele):
                    tableExist = True
                    fields = get_model_field(ele)
                    fields = fields[8:]
                    result = get_model_data(ele)
                    break
                else:
                    result = "Import error!"
        a = 0
        if(result != "Import error!"):
            for x in result:
                final[a] = model_to_dict(x)
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
