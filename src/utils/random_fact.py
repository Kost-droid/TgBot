from random import choice
from src.resource.request_site_ai import make_request


directs = ['исторический факт','научный факт', 'географический факт', 'культурный факт']

list_facts = [('data_random_fact/kalina.jpg', 'Ты эксперт по ягодам. Приведи один интересный факт о ягоде калина'),
              ('data_random_fact/winter.jpg', 'Ты эксперт по климату. Приведи один интересный факт о зиме в сибири'),
              ('data_random_fact/autum.jpg', 'Ты эксперт по климату. Приведи один интересный факт об осене в сибири'),
              ('data_random_fact/горы.jpg', 'Ты эксперт по горам. Приведи интересный факт о горах'),
              ('data_random_fact/гриб_мухомор.jpg', 'Ты эксперт по грибам.Приведи интересный факт о мухоморах'),
              ('data_random_fact/грибы_опята.jpg', 'Ты эксперт по грибам.Приведи интересный факт об опятах'),
              ('data_random_fact/кедровая_шишка.jpg', 'Ты эксперт по шишкам. Приведи интересный факт о шишках'),
              ('data_random_fact/снег.jpg', 'Ты эксперт по климату.Приведи интересный факт о снеге'),
              ('data_random_fact/ягода_смородина.jpg', 'Приведи интересный факт о смородине')]


def get_fact():

    fact = choice(list_facts)

    addition = f"По направлению {choice(directs)}. Не более 150 символов на твой ответ."

    message = [{
                "role": "system",
                "text": fact[1] + addition
            }]
    try:
        result = make_request(message)
    except MemoryError as error:
        raise error
    else:
        return fact[0], result

