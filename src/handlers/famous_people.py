from aiogram import Router
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from src.utils.yandex_ai import YandexAi, list_famous_people
from src.keyboards.coreer_keyboards import make_row_keyboard
from src.keyboards.keyboards import kb1
from src.exception_handlers.my_exception import MyException

router = Router()

ai_person = YandexAi()

class CareerChoice(StatesGroup):
    person = State()
    talk = State()

# обработка команды разговор
@router.message(F.text == 'Разговор')
async def command_talk(message: types.Message, state: FSMContext):
    await message.answer('Выберите персону', reply_markup= make_row_keyboard(list_famous_people, 3))
    await state.set_state(CareerChoice.person)


# если персона выбрана представляется и предлагает общение
@router.message(CareerChoice.person, F.text.in_(list_famous_people))
async def set_person(message: types.Message, state: FSMContext):
    ai_person.set_person(message.text)
    try:
        await message.answer(ai_person.get_ai_answer(), reply_markup= make_row_keyboard(['Стоп'], 1))
    except MyException:
        await mistake(message, state)
    else:
        await state.set_state(CareerChoice.talk)


# если сообщение не из списка персон предлагает выбрать персону
@router.message(CareerChoice.person)
async def choice_person_incorrect(message: types.Message, state: FSMContext):
    # await message.answer('Выберите персону', reply_markup= make_row_keyboard(list_famous_people))
    await command_talk(message, state)


# обработка команды стоп
@router.message(CareerChoice.talk, F.text == 'Стоп')
async def send_quest(message: types.Message, state: FSMContext):
    ai_person.reset()
    await message.answer(text="До свидания !", reply_markup= kb1)
    await state.clear()


# принимает вопрос пользователя и возвращает ответ персоны
@router.message(CareerChoice.talk)
async def send_quest(message: types.Message):
    ai_person.add_user_quest(message.text)
    await message.answer(text=ai_person.get_ai_answer(), reply_markup= make_row_keyboard(['Стоп'], 1))



# выводит сообщение при ошибке
async def mistake(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(f"Абонент не доступен !\n Попробуйте позднее 😌!",reply_markup=kb1)


