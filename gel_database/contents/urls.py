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
    url(r'^simulation/$',views.showsimulation, name="simulation"),
    url(r'^analysis/$',views.showanalysis, name="analysis"),
    url(r'^analysis/ACTB$',views.showiframe, name="ACTB"),
    url(r'^template/$',views.showtemplate),
    #url(r'^experiment/$',views.showexperiment, name="experiment"),
    url(r'^experiment/$',views.select_data, name="experiment"),
    url(r'^experiment/score200317/', views.score200317),
    url(r'^experiment/score201016/', views.score201016),
    url(r'^experiment/ctvalues200317/', views.ctvalues200317),
    url(r'^experiment/foldchanges200317/', views.foldchanges200317),
    url(r'^experiment/parameter200317/', views.parameter200317),
    url(r'^experiment/parameter201016/', views.parameter201016),
    
]

