from aiogram import F, Router
from aiogram.types import Message
from src.resource.request_site_fox import fox
from src.keyboards.keyboards import kb1, kb2
from src.exception_handlers.my_exception import MyException


router = Router()


# ответ на команду /start
@router.message(F.text == '/start')
async def command_start_handler(message: Message) -> None:
    user_name = message.chat.first_name
    await message.answer(f"Привет, {user_name}!", reply_markup= kb1)

# ответ на команду Старт
@router.message(F.text == 'Старт')
async def command_start_handler(message: Message) -> None:
    user_name = message.chat.first_name
    await message.answer(f"Привет, {user_name}!", reply_markup= kb1)


# ответ на команду стоп
@router.message(F.text == 'Стоп')
async def command_stop_handler(message: Message) -> None:
    user_name = message.chat.first_name
    await message.answer(f"До свидания, {user_name}!", reply_markup= kb2)


# ответ на команду лиса
@router.message(F.text == 'Лиса')
async def command_fox_handler(message: Message) -> None:
    try:
        image_fox = fox()
        await message.answer_photo(image_fox)
    except MyException:
        await mistake(message)
    except Exception:
        MyException()
        await mistake(message)


# эхо бот
@router.message(F.text)
async def echo_handler(message: Message) -> None:
    await message.answer(message.text)


# обработка ошибок запросов
async def mistake(message: Message):
    await message.answer(f"Лисичек пока нет! 😺", reply_markup=kb1)
