from django.shortcuts import render, redirect
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .models import * 



def login(request):
    users= user.objects.all().values()
    if request.method == 'POST':
        inputUser = request.POST.get("usernamefield")
        inputPass = request.POST.get("passwordfield")


        #checking username
        check = user.objects.filter(username = inputUser).exists()
        if check == True:

            #checking password
            check2 = user.objects.filter(username = inputUser, password= inputPass).exists()
            if check2 == True:
                Id = (user.objects.get(username = inputUser, password= inputPass).id)
                request.session['userID'] = Id
                return redirect('homePage', Id ) #REDIRECTS USE THE NAME IN URLS
            else:
                messages.error(request = request,message="Your password is incorrect! Please try again.")

                #space
        else:
            messages.error(request= request, message="This user does not exist! Please try again.")

    Qcontext = {'users': users}
    template = loader.get_template('login.html')
    return HttpResponse(template.render(request=request, context= Qcontext))

def homePage(request, userID):
    data = {"ID": userID}
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render(context= data))

def forum(request, userID):
    data = {"ID": userID}
    template = loader.get_template('forum.html')
    return HttpResponse(template.render(context= data))