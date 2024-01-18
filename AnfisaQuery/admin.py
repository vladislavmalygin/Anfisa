from django.contrib import admin
from .models import AnfisaDatabase
from .models import TimeZones
from .models import QueryDatabase
from .models import AnswerDatabase

# Register your models here.
admin.site.register(AnfisaDatabase)
admin.site.register(TimeZones)
admin.site.register(QueryDatabase)
admin.site.register(AnswerDatabase)
