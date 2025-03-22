from src.utils.quiz_ai import list_themas
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from src.keyboards.coreer_keyboards import make_row_keyboard
from aiogram.types import ReplyKeyboardRemove
from src.utils.quiz_ai import QuestsAI
from src.keyboards.keyboards import kb1
from src.exception_handlers.my_exception import MyException



router = Router()

quests_ai = QuestsAI()

class CareerChoice(StatesGroup):
    choice_thema = State()
    await_answer = State()
    next_quest = State()


# обработка команды викторина
@router.message(F.text == 'Викторина')
async def command_random(message: Message, state: FSMContext):
    await message.answer(text= 'Выберите тему!', reply_markup= make_row_keyboard(list_themas, 3))
    await state.set_state(CareerChoice.choice_thema)


# получение вопроса ИИ на выбранную тему
@router.message(CareerChoice.choice_thema, F.text.in_(list_themas))
async def get_quest_from_ai(message: Message, state: FSMContext):
    quests_ai.set_subject(message.text)
    try:
        await message.answer(text= quests_ai.get_guest(), reply_markup= ReplyKeyboardRemove())
    except MyException:
        await mistake(message, state)
    else:
        await state.set_state(CareerChoice.await_answer)

# если тема не соответствует предложенному списку возвращает на выбор темы
@router.message(CareerChoice.choice_thema)
async def incorrect_thema(message: Message, state: FSMContext):
    await command_random(message, state)


@router.message(CareerChoice.await_answer)
async def get_check_from_ai(message: Message, state: FSMContext):
    try:
        await message.answer(text= quests_ai.get_check_answer(message.text),
                             reply_markup= make_row_keyboard(['Еще вопрос', 'Сменить тему', 'Стоп'], 3))
    except MyException:
        await  mistake(message, state)
    else:
        await state.set_state(CareerChoice.next_quest)


@router.message(CareerChoice.next_quest, F.text == 'Сменить тему')
async def other_topic(message: Message, state: FSMContext):
    await command_random(message, state)


@router.message(CareerChoice.next_quest, F.text == 'Еще вопрос')
async def next_quest(message: Message, state: FSMContext):
    try:
        await message.answer(text=quests_ai.get_guest(), reply_markup=ReplyKeyboardRemove())
    except MyException:
        await mistake(message, state)
    else:
        await state.set_state(CareerChoice.await_answer)


@router.message(CareerChoice.next_quest, F.text == 'Стоп')
async def stop_quest(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text='До свидания !', reply_markup= kb1)


# выводит сообщение при ошибке
async def mistake(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(f"Что-то пошло не так! 😊", reply_markup=kb1)