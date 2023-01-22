from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.

def neponyatno_cho(request):
    return HttpResponse("<h1>Здесь будет мой сайт</h1>\n"
                        "<h5>Или игра</h5>")
def ccylka(request):
    return HttpResponse("<img src='#'> </img>")




