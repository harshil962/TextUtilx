from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,'index.html')

def analyze(request):
    # get text
    djtext = request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover =request.POST.get('newlineremover','off')
    extraspaceremover =request.POST.get('extraspaceremover','off')
    charcount =request.POST.get('charcount','off')
    

    if removepunc == "on":
        punctuations ='''.,;:?!()[]{}<>/\|@#$%^&*_~=+-`'"'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'Removed punctuations','analyzed_text': analyzed}
        djtext =analyzed

        # return render(request,'analyze.html',params)
    
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()

        params={'purpose':' changed to UPPERCASE','analyzed_text': analyzed}
        djtext =analyzed
        # return render(request,'analyze.html',params)

    if(extraspaceremover=="on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed=analyzed + char

        params={'purpose':' changed to UPPERCASE','analyzed_text': analyzed}
        djtext =analyzed
        # return render(request,'analyze.html',params)
    
    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if(char!= "\n") and char!="\r":
                analyzed=analyzed + char

        params={'purpose':' changed to UPPERCASE','analyzed_text': analyzed}
        djtext =analyzed
        # return render(request,'analyze.html',params)
    
    if(charcount=="on"):
        analyzed=""
        analyzed = f"Total number of characters: {len(djtext)}\n"
        analyzed=analyzed+djtext

        params={'purpose':'character count','analyzed_text': analyzed}
        
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and charcount=="on"):
        return render(request,'error.html')
    return render(request,'analyze.html',params)


def error(request):
    context = {'error': 'You must enter some text before submitting the form.'}
    return render(request,'error.html',context)