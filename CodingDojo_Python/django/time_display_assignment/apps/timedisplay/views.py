from django.shortcuts import render, HttpResponse
from datetime import datetime
def index(request):  #listens for requests
    context = {
    'date' : datetime.now()
    }
    print "******"
    return render(request,'timedisplay/index.html', context)

# Create your views here.

# def yourMethodFromUrls(request):
#     context = {
#     'date' : datetime.now()
#     }
#     print "******",data.values()
#     return render(request,'timedisplay/index.html', context)
