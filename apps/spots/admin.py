from django.contrib import admin

# Register your models here.
from .models import PublicUser, Organization, Catparking, Parkingspot, Getdata

admin.site.register(PublicUser)


admin.site.register(Organization)
admin.site.register(Catparking)
admin.site.register(Parkingspot)
admin.site.register(Getdata)
