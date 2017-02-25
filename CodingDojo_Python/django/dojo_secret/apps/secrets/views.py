from django.shortcuts import render, redirect, HttpResponse
from .models import User, Secret
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, "secrets/index.html")

def register(request):
    if request.method == "GET":
        return redirect("/")
    newuser = User.objects.register(request.POST)# this line communicates with the model.py file
    print newuser
    if newuser[0] == False:
        for each in newuser[1]:
            messages.error(request, each)#for each error in the array, make a message for each one
        return redirect("/")
    if newuser[0] == True:
        messages.success(request, 'Successfully registred')
        request.session['userid'] = newuser[1].id
        return redirect ('/secrets')

def secrets(request):
    if 'userid' not in request.session:
        messages.error(request,'Must Login or Register')
        return redirect("/")
    context = {
        'user': User.objects.get(id=request.session['userid']),
        'secrets': User.objects.all()
    }
    print context ['user'].id, context ['user'].first_name, context ['user'].last_name
    return render(request, 'secrets/secrets.html', context)

def validate(request):
    if 'userid' not in request.session:
        return redirect("/")
    if request.method == "POST":
        user = user.objects.get(id=request.session['userid'])
        newmessage = Secret.Secretmanager.validate(request.POST, user)#this line goes to model.py file
        if newmessage[0] == False:
            for each in newmessage[1]:
                message.error(request, each)
                return redirect('/secrets')
        if newmessage[0] == True:
            print newmessage[1]
            return redirect('/secrets')

def login(request):
    if request.method == "GET":
        messages.errors(request, "Must Log in or Register")
        return redirect("/")
    else:
        user = User.objects.login(request.POST) #this line talks to models.py
        print user
        if user[0] == False:
            for each in user[1]:
                messages.add_message(request, messages.INFO, each)
            return redirect ("/")
        if user[0] == True:
            messages.add_message(request, messages.INFO, 'Welcome You are logged in')
            request.session['userid'] = user[1].id #puts the user in session
            return redirect ('/secrets')

def logout(request):
    if 'userid' not in request.session:
        return redirect('/')
    print "*******"
    print request.session['userid']
    del request.session['userid']
    return redirect('/')

# def postsecret(request):
#     if 'userid' not in request.session:
#         messages.error(request, 'Must be logged in, or registered')
#         return redirect("/")#user has to be in session to post a secret
#     secret = Secret.Secretmanager.validate(request.POST['makesecret'])#this line takes the request.POST to the models.py
#     if 'error' in secret:
#         messages.error(request, "Secret field must not be blank")
#         return redirect("/secrets")
#     else:
#         Secret.Secretmanager.create(content=request.POST['makesecret'], creator=User.userManage.get(id=request.session['userid']))
#         return redirect('/secrets')
