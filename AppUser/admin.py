from django.contrib import admin

from AppUser.models import User, Country
from blog.models import Category, Post

# Register your models here.

admin.site.register(User)
admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Post)