import requests
from src.config import token_yandex_ai, id_yandex_ai_catalog
from src.exception_handlers.my_exception import MyException

# для запроса в яндекс
URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
MODEL_URL = f"gpt://{id_yandex_ai_catalog}/yandexgpt-lite"
DATA = {"modelUri": MODEL_URL, "completionOptions": {"stream": False, "temperature": 0.6, "maxTokens": "100"}}
HEADERS = {"Content-Type": "application/json", "Authorization": f"Api-Key {token_yandex_ai}"}



def make_request(messages: []):
    data_request = DATA
    data_request["messages"] = messages
    try:
        response = requests.post(URL, headers=HEADERS, json=data_request)
        response.raise_for_status()
        result  = response.json()
        result = result.get('result').get('alternatives')[0].get('message').get('text')
    except Exception as error:
        raise MyException(f"Тип ошибки - {type(error)}")
    return result