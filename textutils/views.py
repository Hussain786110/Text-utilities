#I have created this file 
from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1> Hussain </h1>
                            <a href ="https://github.com/"> GitHub </a>''')

def about(request):
    return HttpResponse("<h1>This is about hussain</h1>")