from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Hello, world. Kamu sedang berada di students page')


def detail(request, id):
    return HttpResponse('Hello, %s' % id)
