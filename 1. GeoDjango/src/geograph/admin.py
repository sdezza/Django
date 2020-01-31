from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from .models import Agent, ZI

@admin.register(Agent)
class AgentAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')

@admin.register(ZI)
class ZiAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')