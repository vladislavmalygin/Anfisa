from django.shortcuts import render

from .forms import AnfisaDatabaseForm
from .models import AnfisaDatabase
from .models import QueryDatabase
from .forms import QueryDatabaseForm
import datetime as dt
import requests
from .models import TimeZones
from .AnfisaLogic import  format_count_friends,what_time,what_weather,process_anfisa,process_friend,process_query





# Create your views here.
def index(request):
    names = AnfisaDatabase.objects.order_by('-id')[:5]
    if request.method == 'POST':
        form = AnfisaDatabaseForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            'Форма была неверной, попробуйте ещё раз'

    form = AnfisaDatabaseForm()
    context = {
        'form': form,
        'title': 'Анфиса',
        'names': names,
    }

    return render(request, 'AnfisaQuery/index.html', context)


def login(request):
    return render(request, 'AnfisaQuery/registration.html')


def about(request):
    return render(request, 'AnfisaQuery/about.html')


def query(request):
    error = ''
    if request.method == 'POST':
        form = QueryDatabaseForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма была неверной'
    queries = QueryDatabase.objects.order_by('-id')
    form = QueryDatabaseForm()




    context = {
        'queries': queries,
        'form': form
    }

    return render(request, 'AnfisaQuery/query.html', context)


