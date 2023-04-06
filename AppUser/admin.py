from django.contrib import admin

from AppUser.models import User, Country

# Register your models here.

admin.site.register(User)
admin.site.register(Country)