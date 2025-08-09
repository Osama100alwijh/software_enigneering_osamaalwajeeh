from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse('hello worder ')
# Create your views here.
