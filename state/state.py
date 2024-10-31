from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    user_phone_number = State()
    region = State()
    sex = State()
    full_name = State()
    year = State()

# todo state yozish