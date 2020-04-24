from django.contrib.auth.models import Group
from django.contrib import admin
from .models import Incidences, Counties
# from django.contrib.gis.db import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class IncidencesAdmin(LeafletGeoAdmin):
	#pass
	list_display =('name','location')

class CountiesAdmin(LeafletGeoAdmin):
	#pass
	list_display =('name_4', 'name_3', 'name_2')

admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(Counties, CountiesAdmin)
