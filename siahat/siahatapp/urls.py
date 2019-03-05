from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hotels', views.hotels, name='hotels'),
    path('restaurants', views.restaurants, name='restaurants'),
    path('attractions', views.attractions, name='attractions'),
    path('hotels/details/<int:id>', views.Hdetails, name='Hdetails'),
    path('restaurants/details/<int:id>', views.Rdetails, name='Rdetails'),
    path('attractions/details/<int:id>', views.Pdetails, name='Pdetails'),
]