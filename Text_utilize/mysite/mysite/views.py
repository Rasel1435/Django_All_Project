# I have Created This web Site

from curses.ascii import HT
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # params = ({"name": "Sheikh Rasel", "Place": "USA"})
    return render(request, 'index.html')


# def about(request):
#     return HttpResponse(" This is About Page")
def ex1(request):
    return render(request, "ex1.html")


def analyzie(request):
    # Get Text
    djtext = (request.POST.get("text", "default"))
    # Check Ckeckbox values
    removepunc = (request.POST.get("removepunc", "off"))
    capitalize = (request.POST.get("capitalize", "off"))
    newlineremover = (request.POST.get("newlineremover", "off"))
    extraspaceremover = (request.POST.get("extraspaceremover", "off"))
    numberremover = request.POST.get('numberremover', 'off')

    # Check which checkbox is on
    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_-~'''
        analyzied = ""
        for char in djtext:
            if char not in punctuations:
                analyzied = analyzied + char

        params = {"purpose": "Remove Punctuations",
                  "analyzied_text": analyzied}
        djtext = analyzied

    # This is for capitalize
    if (capitalize == "on"):
        analyzied = ""
        for char in djtext:
            analyzied = analyzied + char.upper()

        params = {"purpose": "Change to Uppercase",
                  "analyzied_text": analyzied}
        djtext = analyzied

    # Extra Sapce Remover
    if (extraspaceremover == "on"):
        analyzied = ""
        for index, char in enumerate(djtext):
            # It is for if a extraspace is in the last of the string
            if char == djtext[-1]:
                if not(djtext[index] == " "):
                    analyzied = analyzied + char

            elif not(djtext[index] == " " and djtext[index+1] == " "):
                analyzied = analyzied + char

        params = {'purpose': 'Removed NewLines', 'analyzied_text': analyzied}
        djtext = analyzied

    # This is for New Line Remover
    if (newlineremover == "on"):
        analyzied = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzied = analyzied + char

        params = {"purpose": "New Line Remove", "analyzied_text": analyzied}

    if (numberremover == "on"):
        analyzied = ""
        numbers = '0123456789'

        for char in djtext:
            if char not in numbers:
                analyzied = analyzied + char

        params = {"purpose": "Number Remove",
                  "analyzied_text": analyzied}

    if(removepunc != "on" and capitalize != "on" and newlineremover != "on" and extraspaceremover != "on" and numberremover != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, "analyzie.html", params)
