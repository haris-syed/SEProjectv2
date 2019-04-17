from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import *
# Create your views here.

def index(request):

    hotels = Hotels.objects.all()[:4]
    restaurants=Restaurants.objects.all()[:4]
    attractions = Attractions.objects.all()[:4]
    context={
        'hotels':hotels,
        'restaurants':restaurants,
        'attractions':attractions
    }
    return render(request,'siahatapp/index.html',context)

def hotels(request):
    context={}
    if not (request.GET.get('searchbox',False) or request.GET.get('price',False) or request.GET.get('starrating',False)) :
        hotels = Hotels.objects.all()
        context = {
            'hotels':hotels
        }
    else:
        if 'searchbox' in request.GET and (not request.GET['searchbox'] == ''):
            name=request.GET['searchbox']
            hotels=Hotels.objects.filter(name__icontains=name)
            # if(not isinstance(hotels,list)):
            #     hotels=[hotels]
            context = {
            'hotels':hotels
            }
        elif 'price' in request.GET and 'starrating' in request.GET:
            if (not request.GET['price'] == '') and (not request.GET['starrating'] == ''):
                price = int(request.GET['price'])
                starrating=int(request.GET['starrating'])
                #hotels=Hotels.objects.filter(price__lte=price).filter(star_Rating=starrating)
                context = {
                'hotels':hotels
                }
            elif (not request.GET['price'] == ''):
                price = int(request.GET['price'])
                hotels=Hotels.objects.filter(price__lte=price)
                context = {
                'hotels':hotels
                }
            elif (not request.GET['starrating'] == ''):
                starrating=int(request.GET['starrating'])
                hotels=Hotels.objects.filter(star_Rating=starrating)
                context = {
                'hotels':hotels
                }

    
    return render(request,'siahatapp/hotels.html',context)

def restaurants(request):
    context={}
    if not (request.GET.get('searchbox',False) or request.GET.get('cuisine',False) or request.GET.get('starrating',False)) :
        restaurants = Restaurants.objects.all()
        context = {
            'restaurants':restaurants
        }
    else:
        if 'searchbox' in request.GET and (not request.GET['searchbox'] == ''):
            name=request.GET['searchbox']
            restaurants=Restaurants.objects.filter(name__icontains=name)
            # if(not isinstance(hotels,list)):
            #     hotels=[hotels]
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
    restaurant = Restaurants.objects.get(id=id)
    similarrts = Restaurants.objects.all().filter(star_Rating = restaurant.star_Rating).filter(~Q(id=restaurant.id))[:3]
    menu_items = R_menu.objects.filter(restaurant_id__id=id)
    context = {'id':id ,
            'restaurant':restaurant,
            'sim_rts':similarrts,
            'menu_items':menu_items
    }
    return render(request,'siahatapp/Rdetails.html',context)

def Pdetails(request,id):
    attraction = Attractions.objects.get(id=id)
    sim_attractions= Attractions.objects.all().filter(ticket_price__lte=attraction.ticket_price).filter(~Q(id=attraction.id))[:3]
    context = {'id':id,
    'attraction':attraction,
    'sim_attractions':sim_attractions}
    return render(request,'siahatapp/Pdetails.html',context)