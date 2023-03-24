# I have created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get("Text", "default")
    removepunctuation = request.POST.get("removepunc", "Off")
    newlineremove_text = request.POST.get("newlineremover", "Off")
    extraspaceremover_text = request.POST.get("extaspaceremover", "Off")
    uppercase_char = request.POST.get("uppercase", "Off")
    analyzed = ""
    purpose_string = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunctuation == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        djtext = analyzed
        purpose_string += "Remove Punctuation |"

    if uppercase_char == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()

        purpose_string += "Make the Text to Uppercase |"
        djtext = analyzed

    if newlineremove_text == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char

        purpose_string += "Remove the new Lines |"
        djtext = analyzed

    if extraspaceremover_text == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if (index+1) < len(djtext):
                if not (djtext[index] == " " and djtext[index+1] == " "):
                    analyzed += char
            else:
                analyzed += char
        purpose_string += "Remove Extra spaces "
        djtext = analyzed

    if removepunctuation != "on" and uppercase_char != "on" and newlineremove_text != "on" and extraspaceremover_text != "on":
        return HttpResponse("Error")
    else:
        params = {"purpose": purpose_string, "analyzed_text": djtext}
        return render(request, "analyze.html", params)
