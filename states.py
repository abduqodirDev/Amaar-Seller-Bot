from aiogram.fsm.state import StatesGroup, State


class SignUp(StatesGroup):
    phone = State()
