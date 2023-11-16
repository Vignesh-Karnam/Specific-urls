from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Williamson(request):
    return HttpResponse('<h1>Williamson is a man with no haters.</h1>')

def Ravindra(request):
    return HttpResponse('<h1>Rachin Ravindra is a great youngster.</h1>')