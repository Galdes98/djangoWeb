from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index (response):
    return HttpResponse("<b>text test</b>")

def v1 (response):
    return HttpResponse("<b>view 1</b>")