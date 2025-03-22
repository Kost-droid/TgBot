import requests
from src.config import weather_api_key
from src.exception_handlers.my_exception import MyException

APY_KEY = weather_api_key

# возвращает сведения о погоде в выбранном городе
def get_info_weather (city: str):

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APY_KEY}&units=metric'

    try:
        response = requests.get (url)
        response.raise_for_status()
        data = response.json()
    except Exception as error:
        raise MyException ({type(error)})

    return f'City: {data['name']} \nTemp: {data['main']['temp']} \nWeather: {data['weather'][0]['description']}'
