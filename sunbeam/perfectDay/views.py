from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def login(request):
    data = {"x": "x"}
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render(context= data))

def homePage(request):
    data = {"x": "x"}
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render(context= data))

