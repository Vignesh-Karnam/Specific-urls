from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Virat(request):
    return HttpResponse('<h17>Virat has scored his 50th century.</h1>')

def Shreyas(request):
    return HttpResponse('<h1>Shreyas has also scored a century.</h1>')