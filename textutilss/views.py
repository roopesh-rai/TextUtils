# I Have Created This File
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, "one.html")

def about(request):
    return render(request, "two.html")

def boot(request):
    return render(request, "index.html")

def textutils(request):
    return render(request, "text.html")

def contact(request):
    return render(request, "contact.html")

def analize(request):
    djtext = request.POST.get('ta', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    punctuations = '''!()-[]{} ;:'"/,<>.\?@#$%^&*_~'''

    if(removepunc == "on"):
        analized=""
        for char in djtext:
            if char not in punctuations:
                analized=analized+char
        params = {"purpose": "Removed Punctuations", "analized_text": analized}
        djtext=analized

    if(uppercase == "on"):
        analized=""
        for char in djtext:
            analized=analized+char.upper()
        params = {"purpose": "Uppercase", "analized_text": analized}
        djtext=analized

    if(lowercase == "on"):
        analized=""
        for char in djtext:
            analized=analized+char.lower()
        params = {"purpose": "Lowercase", "analized_text": analized}
        djtext=analized

    if(newlineremover == "on"):
        analized=""
        for char in djtext:
            if char != "\n" and char != "\r":
                analized=analized+char
        params = {"purpose": "New Line Remover", "analized_text": analized}
        djtext=analized

    if(extraspaceremover == "on"):
        analized=""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analized = analized + char
        params = {"purpose": "Extra Space Remover", "analized_text":analized}
        djtext=analized

    if(charcounter == "on"):
        analized = ""
        for char in djtext:
            analized = analized + char
        x=len(analized)
        params = {"purpose": "Charactercounts", "analized_text": analized, "length": "Your Data Length is "+str(x)}
    if(removepunc != "on" and uppercase != "on" and lowercase != "on" and newlineremover != "on" and extraspaceremover != "on" and charcounter != "on"):
        return HttpResponse("You Didn't Selected Any Thing Please Select It..")
    return render(request, "analize.html", params)
    # return HttpResponse("Remove Punc <br/><br/><a href='/'>Back</a>")