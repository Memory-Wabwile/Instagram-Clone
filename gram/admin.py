from django.contrib import admin

from gram.models import Comments, Image, Profile

# Register your models here.

admin.site.register(Image)
admin.site.register(Comments)
admin.site.register(Profile)