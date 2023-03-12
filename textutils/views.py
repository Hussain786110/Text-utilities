#I have created this file 
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request,'index.html')

def analyze(request):
    djtext = request.GET.get("Text","default")
    removepunctuation = request.GET.get("removepunc","Off")
    analyzed = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunctuation == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed+=char

    params = {"purpose": "Remove Punctuations","analyzed_text":analyzed}
    return render(request,"analyze.html",params)

