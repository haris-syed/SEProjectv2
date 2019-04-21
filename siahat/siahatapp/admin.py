from django.contrib import admin

# Register your models here.
from .models import Hotels
from .models import Restaurants
from .models import Reviews
from .models import R_menu
from .models import Attractions
from .models import Post

admin.site.register(Hotels)
admin.site.register(Restaurants)
admin.site.register(Reviews)
admin.site.register(R_menu)
admin.site.register(Attractions)
admin.site.register(Post)

