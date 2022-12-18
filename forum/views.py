
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
def forum_1(request):
    return HttpResponse("<h1>ФОРУМ</h1>\n"
                        "<h5>Пишите сюда если хотите(надо забивать чат!)</h5>")



