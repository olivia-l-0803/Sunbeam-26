from django.shortcuts import render, redirect
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .models import * 
from datetime import datetime



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
    allposts= forumpost.objects.all().values()
    data = {"ID": userID,
            "forums": allposts}
    template = loader.get_template('forum.html')

    if request.method == "POST":
        print("hi")
        name = request.POST.get("inputname")
        text = request.POST.get("inputtext") 
        new  = forumpost(authorid= userID, author  = name, text = text)
        new.save()
    return HttpResponse(template.render(request=request, context= data))

def todo(request, userID):
    Todotasks= todotask.objects.filter(authorid = userID, done = False)
    done= todotask.objects.filter(authorid = userID, done = True)
    if request.method == "POST":
        if "taskMarked" in request.POST :
            taskID = request.POST.get("taskMarked")
            task = todotask.objects.get(id= taskID)
            task.done = True
            task.save()
        elif "unsubmit" in request.POST :
            taskID = request.POST.get("unsubmit")
            task = todotask.objects.get(id= taskID)
            task.done = False
            task.save()
        if "submitAdd" in request.POST:
            text = request.POST.get("textInput")
            date = request.POST.get('dateInput')
            new = todotask(authorid=userID, text= text, due=date)
            new.save()
        
    data = {"ID": userID,
            "tasks": Todotasks,
             "done": done }
    template = loader.get_template('todo.html')
    return HttpResponse(template.render(request= request,context= data))

def journal(request, userID):
    yourjournal = journalentry.objects.filter(authorid=userID)

    if request.method == "POST":
        event= request.POST.get("date-event-input")
        text = request.POST.get("journal-text-area")
        rating = request.POST.get("day-rating")

        new = journalentry(authorid = userID, event = event, text = text, rating = rating)
        new.save()

    data = {"ID": userID,
            'journals': yourjournal}
    template = loader.get_template('journal.html')
    return HttpResponse(template.render(request=request, context= data))