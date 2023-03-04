from aiogram.dispatcher.filters.state import State, StatesGroup


class States(StatesGroup):
    start = State()
    lvl_1 = State()
    lvl_2 = State()
    lvl_3 = State()
    lvl_4 = State()
    search = State()
    random = State()