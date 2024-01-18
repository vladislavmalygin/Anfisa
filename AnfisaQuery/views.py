from django.shortcuts import render

from .AnfisaLogic import pre_process_query
from .forms import AnfisaDatabaseForm
from .forms import QueryDatabaseForm
from .models import AnfisaDatabase
from .models import QueryDatabase


# Create your views here.
def index(request):
    names = AnfisaDatabase.objects.order_by('-id')
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

    return render(request, 'AnfisaQuery/main_template.html', context)


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
    queries = QueryDatabase.objects.order_by('-id')[:1]
    form = QueryDatabaseForm()
    answer = 'ответ'

    if request.method == 'POST':
        for query in queries:
            QUERY_BASE = QueryDatabase.objects.order_by('-id')[:1]
            query_get = str(QUERY_BASE)

            answer = pre_process_query(query_get)

    context = {
        'queries': queries,
        'form': form,
        'answer': answer,
    }

    return render(request, 'AnfisaQuery/query.html', context)
