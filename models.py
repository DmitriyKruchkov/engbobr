from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    waiting_for_text = State()