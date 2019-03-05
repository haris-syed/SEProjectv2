from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import *
# Create your views here.

def index(request):
    return render(request,'siahatapp/index.html')

def hotels(request):
    hotels = Hotels.objects.all()
    context = {
            'hotels':hotels
    }
    return render(request,'siahatapp/hotels.html',context)

def restaurants(request):
    restaurants = Restaurants.objects.all()
    context = {
            'restaurants':restaurants
    }
    return render(request,'siahatapp/restaurants.html',context)

def attractions(request):
    attractions = Attractions.objects.all()
    context = {
            'attractions':attractions
    }
    return render(request,'siahatapp/attractions.html',context)

def Hdetails(request,id):
    hotel = Hotels.objects.get(id=id)
    similarHotels = Hotels.objects.all().filter(star_Rating = hotel.star_Rating).filter(~Q(id=hotel.id))[:3]
    context = {'id':id ,
            'hotel':hotel,
            'sim_hotels':similarHotels
    }
    return render(request,'siahatapp/Hdetails.html',context)

def Rdetails(request,id):
    context = {'id':id}
    return render(request,'siahatapp/Rdetails.html',context)

def Pdetails(request,id):
    context = {'id':id}
    return render(request,'siahatapp/Pdetails.html',context)