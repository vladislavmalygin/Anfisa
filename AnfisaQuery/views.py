from django.shortcuts import render

from .forms import AnfisaDatabaseForm
from .models import AnfisaDatabase


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

    return render(request, 'AnfisaQuery/main_template.html', context)


def login(request):
    return render(request, 'AnfisaQuery/registration.html')


def about(request):
    return render(request, 'AnfisaQuery/about.html')


def query(request):

    return render(request,'AnfisaQuery/query.html')

