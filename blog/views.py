from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index (request):
    return render(request, "blog/index.html", {})


def categ(request):
    return HttpResponse('<h1>page1<h1>')