#I have created this file 
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request,'index.html')

def analyze(request):
    djtext = request.GET.get("Text","default")
    removepunctuation = request.GET.get("removepunc","Off")
    print(removepunctuation)
    print(djtext)
    return HttpResponse("Remove Punctuation")

