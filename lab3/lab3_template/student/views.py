from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import now
# def index(request):
#     return render('','student/index.html')
# Create your views here.
def index(request):
    context={'name':'osama abdo alwajeeh',
                                                   'age':20000000,
                                                   'job':'developer',
                                                   'name1':'',
                                                   'date_obj': now()
                                        }
    return render('','student/index1.html',context)