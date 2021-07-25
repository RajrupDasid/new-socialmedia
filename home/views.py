from django.shortcuts import render
from django.http import request
# Create your views here.
def homepage(request):

    context={}
    return render (request,'index.html',context)