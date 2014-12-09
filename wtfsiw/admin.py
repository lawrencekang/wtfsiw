from django.contrib import admin
from wtfsiw.models import User, Location
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'email', 'home_address', 'home_location']
    list_display = ('first_name', 'last_name', 'email')

class LocationAdmin(admin.ModelAdmin):
    fields = ['user', 'business_name', 'address', 'location', 'phone']
    list_display = ('business_name', 'address')
admin.site.register(User, UserAdmin)
admin.site.register(Location, LocationAdmin)