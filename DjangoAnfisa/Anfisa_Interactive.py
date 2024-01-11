import datetime as dt
import requests

DATABASE = dict()
print('Привет, я Анфиса')
print('Ты можешь рассказать мне про своих друзей и города в которых они живут.')
print('Для того чтобы начать или продолжить нажми любую кнопку.')
#print('Если надоест рассказывать про друзей просто напиши "всё".')

while input('Если надоест рассказывать про друзей просто напиши "всё".') != "всё":
    key = input('введите Имя: ')
    value = input('введите Город: ')

    DATABASE[key] = value


print('Теперь ты можешь задать мне вопросы')
print('Можешь задать вопрос обратившись ко мне')
print('Я расскажу сколько у тебя друзей, кто они, и где они.')
print('Ещё ты можешь спросить своих друзей "Который час?" или "Как погода?"')
print('Для этого можешь обратиться к другу по имени.')

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


def format_count_friends(count_friends):
    if count_friends == 1:
        return '1 друг'
    elif 2 <= count_friends <= 4:
        return f'{count_friends} друга'
    else:
        return f'{count_friends} друзей'


def what_time(city):
    offset = UTC_OFFSET[city]
    city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
    f_time = city_time.strftime("%H:%M")
    return f_time


def what_weather(city):
    url = f'http://wttr.in/{city}'
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


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
        return f'У тебя {format_count_friends(count)}.'
    elif query == 'кто мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


def process_friend(name, query):
    if name in DATABASE:
        city = DATABASE[name]
        if query == 'ты где?':
            return f'{name} в городе {city}'
        elif query == 'как погода?':
            return what_weather(city)
        elif query == 'который час?':
            if city not in UTC_OFFSET:
                return f'<не могу определить время в городе {city}>'
            time = what_time(city)
            return f'У меня сейчас {time}'
        else:
            return '<неизвестный запрос>'
    else:
        return f'У тебя нет друга по имени {name}'


def process_query(query):
    elements = query.split(', ')
    if elements[0] == 'Анфиса':
        return process_anfisa(elements[1])
    else:
        return process_friend(elements[0], elements[1])


def runner():
    queries = [
       input('введите вопрос: ')
    ]
    for query in queries:
        print('Вы: ' + query, '-', "Друг: " + process_query(query))
runner()
while input('Анфиса: Если вопросы закончились, напиши "всё"') != 'всё':
    runner()