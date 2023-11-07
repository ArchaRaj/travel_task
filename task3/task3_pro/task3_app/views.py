from django.http import HttpResponse
from django.shortcuts import render
from . models import Task3table

# Create your views here.
def index(request):
    obj= Task3table.objects.all()
    return render(request,"index.html",{'result':obj})

