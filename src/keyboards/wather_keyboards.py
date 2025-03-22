from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def make_inline_keyboard(cities: dict):
    keyboard = []
    number = 0
    keyboards = []
    for key, value in cities.items():

        button = InlineKeyboardButton(text=key, callback_data=value)
        keyboard.append(button)
        number += 1

        if number != 0 and number % 3 == 0:
            number = 0
            keyboards.append(keyboard)
            keyboard = []

    return InlineKeyboardMarkup(inline_keyboard = keyboards)