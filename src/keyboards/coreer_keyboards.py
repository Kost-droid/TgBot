from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def make_row_keyboard(buttons: list[str], size: int) -> ReplyKeyboardMarkup:

    keyboard = []
    number = 0
    keyboards = []
    for button in buttons:
        keyboard.append(KeyboardButton(text= button))
        number += 1

        if number != 0 and number % size == 0:
            number = 0
            keyboards.append(keyboard)
            keyboard = []

    return ReplyKeyboardMarkup(keyboard=keyboards, resize_keyboard=True)