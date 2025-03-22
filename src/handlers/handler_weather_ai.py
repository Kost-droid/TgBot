from src.keyboards.wather_keyboards import make_inline_keyboard
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from src.utils.weather_ai import list_citys, get_weather
from src.keyboards.keyboards import kb1
from src.exception_handlers.my_exception import MyException


router = Router()


class CareerChoice(StatesGroup):
    choice_city = State()

# ответ на команду Погода
@router.message(F.text == 'Погода')
async def command_weather(message: Message, state: FSMContext):
    await message.answer(text='Выберите город', reply_markup= ReplyKeyboardRemove())
    await message.answer(text='Из списка', reply_markup= make_inline_keyboard(list_citys))
    await state.set_state(CareerChoice.choice_city)


# возращает результат - погоду в выбранном городе
@router.callback_query(CareerChoice.choice_city)
async def callback_city(callback: CallbackQuery, state: FSMContext):
    city = callback.data
    try:
        await callback.message.answer(get_weather(city), reply_markup=kb1)
    except MyException:
        await mistake(callback, state)
    else:
        await state.clear()


# если города нет в списке возвращает в меню выбора города
@router.message(CareerChoice.choice_city)
async def incorrect_city(message: Message, state: FSMContext):
    await command_weather(message, state)


# выводит сообщение при ошибке
async def mistake(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer(f"Пока не можем сообщить о погоде! "
                                  f"Просто одевайтесь теплее 😊 !",reply_markup=kb1)

