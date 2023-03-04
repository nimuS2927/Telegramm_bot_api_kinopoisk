from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_kb_lvl_0() -> InlineKeyboardMarkup:
    """ Создаем клавиатуру 0-го уровня"""
    kb_lvl_0 = InlineKeyboardMarkup(resize_keyboard=True)
    kb_lvl_0.row(InlineKeyboardButton(text='Фильмы', callback_data="movie"),
                 InlineKeyboardButton(text='Сериалы', callback_data="tv-series"),
                 InlineKeyboardButton(text='Аниме', callback_data="anime")
                 )
    kb_lvl_0.row(InlineKeyboardButton(text='Мультфильмы', callback_data="cartoon"),
                 InlineKeyboardButton(text='Аниме сериалы', callback_data="animated-series")
                 )
    return kb_lvl_0


def get_kb_lvl_1() -> InlineKeyboardMarkup:
    """ Создаем клавиатуру 1-го уровня"""
    kb_lvl_1 = InlineKeyboardMarkup(resize_keyboard=True)
    kb_lvl_1.row(InlineKeyboardButton(text='Жанры', callback_data="genres.name"),
                 InlineKeyboardButton(text='Рейтинг', callback_data="rating.imdb"),
                 InlineKeyboardButton(text='Год', callback_data="year")
                 )
    kb_lvl_1.row(InlineKeyboardButton(text='Назад', callback_data="back_0"))
    kb_lvl_1.row(InlineKeyboardButton(text='Далее', callback_data="next_0"),
                 # InlineKeyboardButton(text='тест', callback_data="test")
                 )
    return kb_lvl_1


def get_kb_lvl_2() -> InlineKeyboardMarkup:
    """ Создаем клавиатуру 2.1 уровня"""
    kb_lvl_2 = InlineKeyboardMarkup(resize_keyboard=True)
    kb_lvl_2.row(InlineKeyboardButton(text='Аниме', callback_data="аниме"),
                 InlineKeyboardButton(text='Биографии', callback_data="биография"),
                 InlineKeyboardButton(text='Боевики', callback_data="боевик"),
                 InlineKeyboardButton(text='Вестерны', callback_data="вестерн")
                 )
    kb_lvl_2.row(InlineKeyboardButton(text='Военные', callback_data="военный"),
                 InlineKeyboardButton(text='Детективы', callback_data="детектив"),
                 InlineKeyboardButton(text='Детские', callback_data="детский"),
                 InlineKeyboardButton(text='Документальные', callback_data="документальный")
                 )
    kb_lvl_2.row(InlineKeyboardButton(text='Драмы', callback_data="драма"),
                 InlineKeyboardButton(text='Игры', callback_data="игра"),
                 InlineKeyboardButton(text='Исторические', callback_data="история"),
                 InlineKeyboardButton(text='Комедии', callback_data="комедия")
                 )
    kb_lvl_2.row(InlineKeyboardButton(text='Короткометражки', callback_data="короткометражка"),
                 InlineKeyboardButton(text='Криминал', callback_data="криминал"),
                 InlineKeyboardButton(text='Мелодрамы', callback_data="мелодрама"),
                 InlineKeyboardButton(text='Музыкальные', callback_data="музыка")
                 )
    kb_lvl_2.row(InlineKeyboardButton(text='Мультфильмы', callback_data="мультфильм"),
                 InlineKeyboardButton(text='Мюзиклы', callback_data="мюзикл"),
                 InlineKeyboardButton(text='Приключения', callback_data="приключения"),
                 InlineKeyboardButton(text='Реальное ТВ', callback_data="реальное ТВ")
                 )
    kb_lvl_2.row(InlineKeyboardButton(text='Семейные', callback_data="семейный"),
                 InlineKeyboardButton(text='Спортивные', callback_data="спорт"),
                 InlineKeyboardButton(text='ТОК-ШОУ', callback_data="ток-шоу"),
                 InlineKeyboardButton(text='Триллеры', callback_data="триллер")
                 )
    kb_lvl_2.row(InlineKeyboardButton(text='Ужасы', callback_data="ужасы"),
                 InlineKeyboardButton(text='Фантастика', callback_data="фантастика"),
                 InlineKeyboardButton(text='Фильмы-нуар', callback_data="фильм-нуар"),
                 InlineKeyboardButton(text='Фэнтези', callback_data="фэнтези")
                 )
    kb_lvl_2.row(InlineKeyboardButton(text='Далее', callback_data="next_1"),
                 InlineKeyboardButton(text='Назад', callback_data="back_1"),
                 # InlineKeyboardButton(text='тест', callback_data="test")
                 )
    return kb_lvl_2


def get_kb_lvl_3() -> InlineKeyboardMarkup:
    """ Создаем клавиатуру 2.2 уровня"""
    kb_lvl_3 = InlineKeyboardMarkup(resize_keyboard=True)
    kb_lvl_3.row(InlineKeyboardButton(text='1', callback_data="1"),
                 InlineKeyboardButton(text='2', callback_data="2"),
                 InlineKeyboardButton(text='3', callback_data="3"),
                 InlineKeyboardButton(text='4', callback_data="4"),
                 InlineKeyboardButton(text='5', callback_data="5"))
    kb_lvl_3.row(InlineKeyboardButton(text='6', callback_data="6"),
                 InlineKeyboardButton(text='7', callback_data="7"),
                 InlineKeyboardButton(text='8', callback_data="8"),
                 InlineKeyboardButton(text='9', callback_data="9"),
                 InlineKeyboardButton(text='10', callback_data="10")
                 )
    kb_lvl_3.row(InlineKeyboardButton(text='Далее', callback_data="next_1"),
                 InlineKeyboardButton(text='Назад', callback_data="back_1"),
                 # InlineKeyboardButton(text='тест', callback_data="test")
                 )
    return kb_lvl_3


def get_kb_lvl_4() -> InlineKeyboardMarkup:
    """ Создаем клавиатуру 2.3 уровня"""
    kb_lvl_4 = InlineKeyboardMarkup(resize_keyboard=True)
    kb_lvl_4.row(InlineKeyboardButton(text='2023', callback_data="2023"),
                 InlineKeyboardButton(text='2022', callback_data="2022"),
                 InlineKeyboardButton(text='2021', callback_data="2021"),
                 InlineKeyboardButton(text='2020', callback_data="2020"),
                 InlineKeyboardButton(text='2019', callback_data="2019"),
                 InlineKeyboardButton(text='2018', callback_data="2018"),
                 InlineKeyboardButton(text='2017', callback_data="2017")
                 )
    kb_lvl_4.row(InlineKeyboardButton(text='2016', callback_data="2016"),
                 InlineKeyboardButton(text='2015', callback_data="2015"),
                 InlineKeyboardButton(text='2014', callback_data="2014"),
                 InlineKeyboardButton(text='2013', callback_data="2013"),
                 InlineKeyboardButton(text='2012', callback_data="2012"),
                 InlineKeyboardButton(text='2011', callback_data="2011"),
                 InlineKeyboardButton(text='2010', callback_data="2010")
                 )
    kb_lvl_4.row(InlineKeyboardButton(text='2020-е', callback_data="2020-2023"),
                 InlineKeyboardButton(text='2010-е', callback_data="2010-2019")
                 )
    kb_lvl_4.row(InlineKeyboardButton(text='2000-е', callback_data="2000-2009"),
                 InlineKeyboardButton(text='1990-е', callback_data="1990-1999"),
                 InlineKeyboardButton(text='1980-е', callback_data="1980-1989"),
                 InlineKeyboardButton(text='1970-е', callback_data="1970-1979")
                 )
    kb_lvl_4.row(InlineKeyboardButton(text='1960-е', callback_data="1960-1969"),
                 InlineKeyboardButton(text='1950-е', callback_data="1950-1959"),
                 InlineKeyboardButton(text='1940-е', callback_data="1940-1949"),
                 InlineKeyboardButton(text='1930-е', callback_data="1930-1939")
                 )
    kb_lvl_4.row(InlineKeyboardButton(text='1920-е', callback_data="1920-1929"),
                 InlineKeyboardButton(text='1910-е', callback_data="1910-1919"),
                 InlineKeyboardButton(text='1900-е', callback_data="1900-1909"),
                 InlineKeyboardButton(text='1890-е', callback_data="1890-1899")
                 )
    kb_lvl_4.row(InlineKeyboardButton(text='Далее', callback_data="next_1"),
                 InlineKeyboardButton(text='Назад', callback_data="back_1")
                 )
    return kb_lvl_4
