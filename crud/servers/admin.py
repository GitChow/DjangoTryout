from django.contrib import admin

# Register your models here.
from servers.models import Server

admin.site.register(Server)