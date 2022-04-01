from django.http import HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("this is my homepage")
    # context is a set of variables 
    context = {
        'variable1': "I am great",
        'variable2': "no one is great"
    }
    return render(request, "index.html", context)

def about(request):
    #return HttpResponse("this is my about homepage")
    return render(request, "about.html")

def services(request):
    #return HttpResponse("this is my services page")
    return render(request, "services.html")

def contact(request):
    #return HttpResponse("this is my contacts page")
    return render(request, "contact.html")

