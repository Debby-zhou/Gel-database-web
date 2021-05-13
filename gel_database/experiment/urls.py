from django.urls import path, re_path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.showexperiment), 
    url('^result/',views.show_experiment_result, name="result"),
]
