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
    url('^experiment/result/',views.show_experiment_result, name="result"),
    
    
]

