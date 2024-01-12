from django.contrib import admin
from.models import AnfisaDatabase
from.models import TimeZones
from.models import QueryDatabase
# Register your models here.
admin.site.register(AnfisaDatabase)
admin.site.register(TimeZones)
admin.site.register(QueryDatabase)
