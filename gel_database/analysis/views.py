from django.shortcuts import render,HttpResponseRedirect,Http404,HttpResponse
from django.contrib import auth
import os
from analysis.forms import SelectGene
from .models import *
from django.forms.models import model_to_dict
import csv

def logout(request):
    auth.logout(request)
    return render(request,'index.html')

tissues = ['other','control','selfrenewal','mesoderm','mesendoderm','ectoderm','endoderm']
def showanalysis(request):
    tissue = [i.capitalize() for i in tissues]
    tissues_gene = [i.capitalize()+'gene' for i in tissues]
    category_r = {}
    gene_r = {}
    try:
        if 'category' in request.POST:
            category_r['result'] = request.POST.get('category')
            if request.method == 'POST':
                    if category_r['result']:
                        form = SelectGene(request.POST)
                        for ele in tissue:
                            if category_r['result'] == ele:
                                formName = ele + 'gene'
                                form = SelectGene(request.POST)[formName]
        else:
            r = list(request.POST)
            for ele,v in zip(tissues_gene,tissues):
                if ele in request.POST:
                    form = SelectGene(request.POST)[ele]
                    gene_r['result'] = request.POST[ele]
                    fileName = "/static/assets/model/scorecard/ct_value_/" + v + "/interpolate/" + gene_r['result'] +".html" 
    except:
        form = SelectGene()['Controlgene']
    return render(request, 'analysis.html', locals())
