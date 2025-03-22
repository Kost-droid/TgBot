from aiogram import types


button_1 = types.KeyboardButton(text='Профессия')
button_2 = types.KeyboardButton(text='Лиса')
button_3 = types.KeyboardButton(text='Погода')
button_4 = types.KeyboardButton(text='Разговор')
button_5 = types.KeyboardButton(text='Факты')
button_6 = types.KeyboardButton(text='Викторина')
button_7 = types.KeyboardButton(text='Стоп')
button_8 = types.KeyboardButton(text='Старт')


keyboard_1 = [[button_1, button_2], [button_3, button_4], [button_5, button_6], [button_7]]
keyboard_2 = [button_8]


kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard_1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=[keyboard_2], resize_keyboard=True)
