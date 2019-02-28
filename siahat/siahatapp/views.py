from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'siahatapp/index.html')

def hotels(request):
    return render(request,'siahatapp/hotels.html')

def restaurants(request):
    return render(request,'siahatapp/restaurants.html')

def pois(request):
    return render(request,'siahatapp/pois.html')

def Hdetails(request,id):
    context = {'id':id}
    return render(request,'siahatapp/Hdetails.html',context)

def Rdetails(request,id):
    context = {'id':id}
    return render(request,'siahatapp/Rdetails.html',context)

def Pdetails(request,id):
    context = {'id':id}
    return render(request,'siahatapp/Pdetails.html',context)