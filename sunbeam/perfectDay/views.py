from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse



def homePage(request, userID):
    data = {"ID": userID}
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render(context= data))

def JournalPage(request):
    data = {"x": "x"}
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render(context= data))