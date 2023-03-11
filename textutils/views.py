#I have created this file 
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request,'index.html')

def removepunc(request):
    print(request.GET.get("Text"))
    return HttpResponse("Remove Punctuation")

def capitalizefirst(request):
    return HttpResponse('''<a href ='/'>Back</a> 
                            <h1>Capitalize first</h1>''')

def newlineremover(request):
    return HttpResponse("New Line removed")

def spaceremover(request):
    return HttpResponse("Space removeed")

def charactercount(request):
    return HttpResponse("Character Count")