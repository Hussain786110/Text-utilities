#I have created this file 
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Hussain")

def about(request):
    return HttpResponse("<h1>This is about hussain</h1>")