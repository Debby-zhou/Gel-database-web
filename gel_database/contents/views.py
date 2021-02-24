from django.shortcuts import render

# Create your views here.
def showhome(request):
    return render(request, 'home.html')
def showexperiment(request):
    return render(request, 'experiment.html')
def showsimulation(request):
    return render(request, 'simulation.html')
def showanalysis(request):
    return render(request, 'analysis.html')
