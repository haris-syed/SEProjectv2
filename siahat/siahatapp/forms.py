from django import forms
from .models import Hotels
from .models import Restaurants
from bootstrap_datepicker.widgets import DatePicker

class hotel_infoForm(forms.ModelForm):
    class Meta:
        model = Hotels
        fields = ['name','description','url_Picture','address','star_Rating',]

class restaurant_infoForm(forms.ModelForm):
    class Meta:
        model = Restaurants
        fields = ['name','description','opening_Time','url_Picture','address','star_Rating',]
