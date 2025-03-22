from aiogram import Router
from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from src.keyboards.coreer_keyboards import make_row_keyboard
from src.keyboards.keyboards import kb1


router = Router()

available_jobs = [
    'Доктор',
    'Учитель',
    'Рабочий'
]

available_grades = [
    'Стажер',
    'Средний',
    'Мастер'
]


class CareerChoice(StatesGroup):
    job = State()
    grade = State()

# ответ на команду Профессия
@router.message(F.text == 'Профессия')
async def command_prof(message: types.Message, state: FSMContext):
    await message.answer('Выберите профессию !', reply_markup=make_row_keyboard(available_jobs, 3))
    await state.set_state(CareerChoice.job)

# выбор уровня
@router.message(CareerChoice.job, F.text.in_(available_jobs))
async def choice_prof(message: types.Message, state: FSMContext):
    await state.update_data(profession = message.text)
    await message.answer('Выберите Ваш уровень !', reply_markup=make_row_keyboard(available_grades, 3))
    await state.set_state(CareerChoice.grade)

# если выбор не в списке профессий
@router.message(CareerChoice.job)
async def choice_prof_incorrect(message: types.Message, state: FSMContext):
    await command_prof(message, state)


# выводит ответ - выбранная профессия и уровень
@router.message(CareerChoice.grade, F.text.in_(available_grades))
async def choice_grade(message: types.Message, state: FSMContext):
    await state.update_data(grade = message.text)
    user = await  state.get_data()
    await message.answer(text=f'Ваша профессия {user['profession']}. Ваш уровень {user['grade']} 😄.',
                         reply_markup= kb1)
    await state.clear()

# если выбор не в списке уровней предлагает выбрать уровень
@router.message(CareerChoice.grade)
async def choice_grade_incorrect(message: types.Message, state: FSMContext):
    await message.answer('Выберите Ваш уровень !', reply_markup=make_row_keyboard(available_grades, 3))
    await state.set_state(CareerChoice.grade)
