"""gel_database URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.showhome), 
    url('logout/$',views.logout, name="logout"),
    url('^simulation/$',views.showsimulation, name="simulation"),
    url('^analysis/$',views.showanalysis, name="analysis"),
    url('^analysis/scorecard/',views.select_result, name="scorecard"),
    url('^template/$',views.showtemplate),
    url('^experiment/$',views.showexperiment, name="experiment"),
    url('^experiment/results/',views.show_experiment_result, name="expresults"),
    #url('^experiment/score200317/', views.score200317, name="score200317"),
    #url('^experiment/score201016/', views.score201016, name="score201016"),
    #url('^experiment/ctvalues200317/', views.ctvalues200317, name="ctvalues200317"),
    #url('^experiment/foldchanges200317/', views.foldchanges200317, name="foldchanges200317"),
    #url('^experiment/parameter200317/', views.parameter200317, name="parameter200317"),
    #url('^experiment/parameter201016/', views.parameter201016, name="parameter201016"),
    
]

