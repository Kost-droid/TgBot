from src.utils.random_fact import get_fact
from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from src.keyboards.coreer_keyboards import make_row_keyboard
from src.keyboards.keyboards import kb1
from src.exception_handlers.my_exception import MyException


router = Router()


class CareerChoice(StatesGroup):
    random_facts = State()


# обработка команды факты
@router.message(F.text == 'Факты')
async def command_random(message: Message, state: FSMContext):
    try:
        fact = get_fact()
        await message.answer_photo(FSInputFile(fact[0]))
        await message.answer(text= fact[1], reply_markup= make_row_keyboard(['Еще факт', 'Стоп'], 2))
    except MyException:
        await mistake(message, state)
    except Exception as error:
        MyException()
        await mistake(message, state)
    else:
        await state.set_state(CareerChoice.random_facts)
    

# обработка команды Еще факт
@router.message(CareerChoice.random_facts, F.text == 'Еще факт')
async def next_fact(message: Message, state: FSMContext):
    await command_random(message, state)


@router.message(CareerChoice.random_facts, F.text == 'Стоп')
async def stop_fact(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text='До свидания !', reply_markup= kb1)


# выводит сообщение при ошибке
async def mistake(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(f"Что-то пошло не так! Почитайте пока книгу 😎!", reply_markup=kb1)

