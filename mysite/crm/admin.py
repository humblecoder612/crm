from django.contrib import admin

# Register your models here.

from .models import Clients,User

admin.site.register(User)
admin.site.register(Clients)

