import datetime as dt

import requests

from .models import AnfisaDatabase
from .models import QueryDatabase

answer = str()
DATABASE = AnfisaDatabase.objects.all()
QUERY_BASE = QueryDatabase.objects.all()
query_get = str(QUERY_BASE)
people = AnfisaDatabase.objects.values('name', 'city')
people_dict = {person['name']: person['city'] for person in people}

for obj in DATABASE:
    name_q = str(AnfisaDatabase.objects.values_list('name', flat=True)).replace("<QuerySet [",
                                                                                "").replace("]>", "")
    name_q = name_q.replace('[', '')
for obj in DATABASE:
    city_w = AnfisaDatabase.objects.values_list('city', flat=True)
    city_q = (str(city_w).replace("<QuerySet [", "").replace("]>", "")).replace("'", '')


def pre_process_query(query):
    elements = query.replace("<QuerySet [", "").replace("]>", "")
    return process_query(elements)


def process_query(query):
    elements = query.split(',')
    if elements[0] == 'Анфиса':
        return process_anfisa(elements[1])
    else:
        return process_friend(elements[0], elements[1])


def process_anfisa(query):
    if query == ' сколько у меня друзей?':
        count = len(city_w)
        return f'У тебя {format_count_friends(count)}.'
    elif query == ' кто мои друзья?':
        friends_string = (str(name_q)).replace('<QuerySet', ' ').replace(']>', '').replace("'", '')

        return f'Твои друзья: {friends_string}'
    elif query == ' где мои друзья?':

        cities_string = city_q.replace("'", '')

        return f'Твои друзья в городах: {cities_string}'
    else:
        return f'<неизвестный запрос:>{query}'


def process_friend(name_q, query):
    if AnfisaDatabase.objects.filter(name=name_q).exists():
        city_q = people_dict[name_q]
        if query == ' ты где?':

            return f'{name_q} в городе {city_q}'
        elif query == ' как погода?':
            return what_weather(city_q)
        elif query == ' который час?':
            if city_q not in UTC_OFFSET:
                return f'<не могу определить время в городе {city_q}>'
            time = what_time(city_q)

            return f'У меня сейчас {time}'
        else:

            return '<неизвестный запрос>'
    else:

        return f'У тебя нет друга по имени {name_q}'


def format_count_friends(count_friends):
    if count_friends == 1:
        return '1 друг'
    elif 1 < count_friends < 5:

        return f'{count_friends} друга'
    else:

        return f'{count_friends} друзей'


def what_time(city_q):
    global offset
    if city_q == 'Москва':
        offset = 3
    elif city_q == 'Санкт-Петербург':
        offset = 3
    elif city_q == 'Новосибирск':
        offset = 7
    elif city_q == 'Екатеринбург':
        offset = 5
    elif city_q == 'Москва':
        offset = 3
    elif city_q == 'Нижний Новгород':
        offset = 3
    elif city_q == 'Казань':
        offset = 3

    city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
    f_time = city_time.strftime("%H:%M")

    return f_time


def what_weather(city_q):
    url = f'https://wttr.in/{city_q}'
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:

        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text
    else:

        return '<ошибка на сервере погоды>'


UTC_OFFSET = {
    'Москва': 3,
    'Санкт-Петербург': 3,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Самара': 4,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Воронеж': 3,
    'Пермь': 5,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2,
    'Владивосток': 10
}
