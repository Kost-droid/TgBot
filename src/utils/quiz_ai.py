from src.resource.request_site_ai import make_request
from src.exception_handlers.my_exception import MyException


# список тем
list_themas = ['История','Техника', 'Искуство', 'Животные', 'Растения', 'Космос']


class QuestsAI:

    def __init__(self):
        self.prompt = []
        self.subject = ''
        self.number = 0


    # задает тему вопросов
    def set_subject(self, subject: str):
        self.subject = subject


    # возвращает вопрос по новой теме
    def get_guest(self):

        if self.prompt:
            self.prompt.clear()
        self.prompt.append({
            "role": "system",
            "text": f"Задай вопрос на тему - {self.subject}. Вопрос должен иметь однозначный"
                    f" ответ. Приведи три варианта ответа, из которых два должно быть не правильных а один правильный. "
        })

        try:

            result = make_request(self.prompt)

        except MyException as error:
            raise error

        self.prompt.append({
            "role": "assistant",
            "text": result
        })
        return result


# бот оценивает ответ
    def get_check_answer(self, message: str):
        self.prompt.append({
            "role": "system",
            "text": f"На следующий вопрос с вариантами ответа - {self.prompt[1].get("text")}"
                    f"Пользователь выбрал вариант - {message}! Если ответ пользователя "
                    f"правилный напиши - Это верный ответ! Если ответ пользователя не правильный "
                    f"напиши - Это не правильный ответ !"
            })
        try:
            result = make_request([self.prompt[2]])
        except MyException as error:
            raise error
        else:
            if 'верный' in result:
                self.number +=1
            return result + f'\n Верных ответов - {self.number}'

