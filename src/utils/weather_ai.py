from src.resource.request_site_ai import make_request
from src.resource.request_site_weather import get_info_weather
from src.exception_handlers.my_exception import MyException



prompt = []


list_citys = {'Новосибирск': 'Novosibirsk','Владивосток': 'Vladivostok','Иркутск':'Irkutsk',
              'Лондон':'London', 'Нью-Йорк': 'New York', 'Токио':'Tokyo'}


# возвращает описание погоды и рекомендации
def get_weather (city: str):

    try:
        info = get_info_weather(city)
    except MyException as error:
        raise error

    if prompt:
        prompt.clear()
    prompt.append({
             "role": "system",
             "text": f"Это данные о погоде на текущий момент - {info}. Температуру приведи в целых числах."
                     f"Напиши о них пользователю, обязательно укажи город и все эти показатели."
                     f"А так же дай рекомендации как нужно одеться. И пожелай удачи и хорошего настроения."
         })
    try:
        result = make_request(prompt)
    except MyException as error:
        raise error

    return result

