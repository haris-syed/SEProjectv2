from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ProfilePicture=models.ImageField(default='default.jpg',upload_to='profile_pics')
    Adress = models.CharField(max_length=50,blank=True, null=True)
    Age = models.IntegerField(blank=True, null=True)
    City = models.CharField(max_length=20,blank=True, null=True)
    g_type = (('standard','standard'),
    ('hotel_owner','hotel_owner'),
    ('restaurant_owner','restaurant_owner')
    )
    _type = models.CharField(max_length=7, choices=g_type, default='standard')

    def __str__(self):
        return f'{self.user.username} Profile'



