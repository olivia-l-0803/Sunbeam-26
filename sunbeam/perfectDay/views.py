from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def homePage(request):
    data = {"fuck you": 2}
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render(context= data))

