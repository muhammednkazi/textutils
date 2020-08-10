# this file is made by muhammed
from django.http import HttpResponse

# to show data from template we write the below line.
from django.shortcuts import render


def index(requests):
    # requests is the default argument
    # index.html is the file that we want to send
    return render(requests,'index.html')

#receiving text from homepage
def analyze(request):

    # get the text
    gottext=request.POST.get('text','off')

    # to get the checkbox name and its value
    # if its not checked it will send off
    removepunc=request.POST.get('removepunc','off')
    uppercase=request.POST.get('uppercase','off')
    newlineremove=request.POST.get('newlineremove','off')
    extraspaceremove=request.POST.get('extraspaceremove','off')
    countcharacter=request.POST.get('countcharacter','off')

    # check if checkbox is on
    # if condition for removing punctuations
    if removepunc=="on":
        analyzed_text = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for i in gottext:
            if i not in punctuations:
                analyzed_text = analyzed_text + i
        param = {'purpose':'Remove Punctuations','value': analyzed_text}
        gottext=analyzed_text

    # uppercase the text
    if uppercase=="on":
        analyzed_text = ""
        analyzed_text=gottext.upper()
        param = {'purpose':'Remove Punctuations','value': analyzed_text}
        gottext = analyzed_text

    # remove new lines
    if newlineremove=="on":
        analyzed_text = ""
        for i in gottext:
            if i!="\n" and i!="\r":
                analyzed_text=analyzed_text+i
        param = {'purpose':'Remove New Line','value': analyzed_text}
        gottext = analyzed_text

    # remove extra space
    if extraspaceremove=="on":
        analyzed_text = ""
        for index,char in enumerate(gottext):
            if not(gottext[index]==" " and gottext[index+1]==" "):
                analyzed_text=analyzed_text + char
        param = {'purpose':'Remove Extra Space','value': analyzed_text}
        gottext = analyzed_text

    #to count no. of characters
    if countcharacter=="on":
        analyzed_text = ""
        analyzed_text=len(gottext)
        param = {'purpose':'Total Characters are:-','value': analyzed_text}

    # if no checkbox is checked
    if(countcharacter!="on" and extraspaceremove!="on" and newlineremove!="on" and removepunc!="on" and uppercase!="on"):
        return HttpResponse("Please Select Atleast One Operation")

    # this will return the parameters to the anaylyze.html file
    return render(request, 'analyze.html', param)

# about us page function
def aboutus(request):
    return render(request,'aboutus.html')

# contact us page function
def contactus(request):
    return render(request,'contactus.html')
