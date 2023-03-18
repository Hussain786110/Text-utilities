# I have created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request, 'index.html')


def analyze(request):
    djtext = request.GET.get("Text", "default")
    removepunctuation = request.GET.get("removepunc", "Off")
    uppercase_char = request.GET.get("uppercase", "Off")
    analyzed = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunctuation == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed += char

        params = {"purpose": "Remove Punctuations", "analyzed_text": analyzed}
        return render(request, "analyze.html", params)

    elif uppercase_char == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()

        params = {"purpose": "make the text into upper case",
                  "analyzed_text": analyzed}
        return render(request, "analyze.html", params)


def exercise(request):

    return HttpResponse('''<a href = "www.facebook.com">Facebook</a> <br>
                            <a href = "www.Google.com">Google</a> <br>
                            <a href = "www.Rediff.com">Rediff</a><br>
                            <a href = "www.Yahoo.com">Yahoo</a> <br>''')
