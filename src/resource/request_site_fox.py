import requests
from src.exception_handlers.my_exception import MyException

URL = 'https://randomfox.ca/floof'

def fox():
    try:
        response = requests.get(URL, timeout= 5)
        response.raise_for_status()
    except Exception:
        raise MyException()
    else:
        return response.json().get('image')

