from django.db import models

# Create your models here.
from django_mysql.models import ListTextField
from django.utils import timezone 
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.forms import ModelForm

class Hotels(models.Model):
    name=models.CharField(max_length=100,blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    url_Picture = ListTextField(
        base_field=models.CharField(max_length=100),
        size=100,
    )
    address=models.TextField(blank=True, null=True)
    star_Rating=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Hotels"


class Restaurants(models.Model):
    name=models.CharField(max_length=100,blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    opening_Time=models.TimeField(auto_now_add=True, blank=True)
    url_Picture = ListTextField(
        base_field=models.CharField(max_length=100,blank=True, null=True),
        size=100,
        default='1',
    )
    address=models.TextField(blank=True, null=True)
    star_Rating=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Restaurants"

h_type = (
    ('hotel','HOTEL'),
    ('restaurant', 'RESTAURANT'),
    ('poi','POINT_OF_INTERET'),
)
class Reviews(models.Model):
    author=models.CharField(max_length=100,blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    star_Rating=models.IntegerField(blank=True, null=True)
    _type = models.CharField(max_length=6, choices=h_type, default='hotel')
    type_id=models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural="Reviews"

i_type = (
('food','FOOD'),
('drink', 'DRINK'),
('other','OTHER'),
)
class R_menu(models.Model):
    item_name=models.CharField(max_length=100,blank=True, null=True)
    item_cost=models.IntegerField(blank=True, null=True)
    item_type = models.CharField(max_length=6, choices=i_type, default='food')
    restaurant_id = models.ForeignKey(Restaurants, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name_plural="R_menus"

class Attractions(models.Model):
    name=models.CharField(max_length=100,blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    opening_Time=models.TimeField(auto_now_add=True, blank=True)
    address=models.TextField(blank=True, null=True)
    url_Picture = ListTextField(
         base_field=models.CharField(max_length=100,blank=True, null=True),
        size=100,
        default='1',
    )
    ticket_price=models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Attractions"


class Post(models.Model): 
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=200) 
    text = RichTextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now) 
    published_date = models.DateTimeField(blank=True, null=True) 

    def publish(self): 
        self.published_date = timezone.now() 
        self.save() 

    def __str__(self): 
        return self.title


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','text']