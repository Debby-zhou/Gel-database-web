from django.shortcuts import render,HttpResponseRedirect,Http404,HttpResponse
from django.contrib import auth
import os
from simulation.forms import SelectSimPic
from .models import *
from django.forms.models import model_to_dict
import csv, json

def showsimulation(request):
    models = SimulationResult1227
    final = {}
    # with open('static/assets/simulation/simulation_result_1227.csv', newline='') as csvfile:
    #     rows = csv.reader(csvfile)
    #     next(rows)
    #     rows = list(rows)
    if request.method == "POST":
        form = SelectSimPic(request.POST)
    else:
        form = SelectSimPic()
    if request.POST:
        sim_r = {}
        final_parameter = {}
        final_result = {}
        sim_r['simparameter'] = request.POST.get('simparameter')
        result = get_model_data(models)
        a = 0
        if(result != "Import error!"):
            for x in result:
                final[a] = model_to_dict(x)
                final_parameter[a] = list(final[a].values())[0:6]
                final_result[a] = list(final[a].values())[6:]
                a += 1
    return render(request, 'simulation.html', locals())
def get_model_data(modelName):
    try:
        result = modelName.objects.using('simulationdb').all()
    except:
        result = "Import error!"
    return result
