from src.resource.request_site_ai import make_request
from src.exception_handlers.my_exception import MyException


list_famous_people = ['Ленин', 'Эйнштейн', 'Рей Брэдбери', 'Ван Гог', 'Ньютон', 'Пётр I']

class YandexAi:

    def __init__(self):
        self.prompt = []


    # задает параметр - персона
    def set_person(self, role: str):
        self.prompt.append( {
                "role": "system",
                "text": f"Ты {role}. Представься по Имени Фамилии. Поздоровайся и "
                        f"отвечай на вопрос от его имени {role}. Символов в ответе не более 100."
            })

    #  добавляет в промпт вопрос пользователя
    def add_user_quest(self, quest: str):
        self.prompt.append({
            "role": "user",
            "text": quest
        })

    #  добавляет в промпт ответ персоны
    def add_assistant_answer(self, answer):
        self.prompt.append({
            "role": "assistant",
            "text": answer
        })

    # возвращает ответ персоны
    def get_ai_answer(self):
        try:
            result = make_request(self.prompt)
        except MyException as error:
            raise error

        self.add_assistant_answer(result)
        return result


    def reset(self):
        self.prompt = []

