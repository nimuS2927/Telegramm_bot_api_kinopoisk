from aiogram import types
from create_bot import dp
from keyboard import keyboard_client
from aiogram.dispatcher import FSMContext
from FSMState.FSMState import States
from API.kinopoisk_api import get_movie, get_random_movie
from random import randint
from config import DB_NAME, USER, PASSWORD, HOST
from BaseDate.my_db import create_connection_mysql_db, insert_info
import json

type_base = {
    'movie': 'Фильмы',
    'tv-series': 'Сериалы',
    'anime': 'Аниме',
    'cartoon': 'Мультфильмы',
    'tv-show': 'ТВ шоу',
    'animated-series': 'Аниме сериалы'
}


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Для поиска по категориям воспользуйся командой /search.\n'
                         'Для получения 5 случайных тайтлов воспользуйся командой /random.')
    await States.start.set()


@dp.message_handler(commands=['search'], state=States.all_states)
async def re_search(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Что будем искать?', reply_markup=keyboard_client.get_kb_lvl_0())
    await States.start.set()


@dp.message_handler(commands=['random'], state=States.all_states)
async def search(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Что бы вы хотели получить?', reply_markup=keyboard_client.get_kb_lvl_0())
    await States.random.set()


@dp.callback_query_handler(state=States.random)
async def search_random(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({'type': call.data,
                             'rating.imdb': '6-10'
                             })
    await call.message.answer(f'Твой выбор {type_base[call.data]}, отлично')
    data = await state.get_data()
    str_info_request = f'{type_base[call.data]}|rating.imdb {data["rating.imdb"]}'
    result_search_random = await get_random_movie(data)
    result = json.loads(result_search_random.text)
    my_result = []
    for movie in result['docs']:
        if movie['name'] is not None:
            my_result.append(movie)
    if len(my_result) > 5:
        finish_num = len(my_result) - 5
        start_num = randint(0, finish_num)
        step_num = 5
    else:
        start_num = 0
        step_num = len(my_result)
    str_info_response = ''
    for i_movie in my_result[start_num:start_num + step_num]:
        name = i_movie['name']
        length = i_movie.get("movieLength")
        rating = i_movie.get("rating").get("imdb")
        date = i_movie.get("year")
        description = i_movie.get("shortDescription")
        if length is not None:
            length_str = f'Продолжительность {length} минут'
        else:
            length_str = ''
        if rating is not None:
            rating_str = f'Рейтинг IMDb - {rating}'
        else:
            rating_str = ''
        if date is not None:
            date_str = f'Дата релиза - {date}'
        else:
            date_str = ''
        if description is not None:
            description_str = f'Краткое описание: {description}'
        else:
            description_str = ''
        photo = ''
        if i_movie.get("poster") is not None:
            photo = i_movie["poster"]["url"]
        await call.message.answer(
            f'Название - {name}\n'
            f'{length_str}\n'
            f'{rating_str}\n'
            f'{date_str}\n'
            f'{description_str}\n'
            f'{photo}'
        )
        str_info_response = str_info_response + \
                            f'{name}|{length_str}|{rating_str}|{date_str}|{description_str}|{photo}\n'
    with create_connection_mysql_db(HOST, USER, PASSWORD, DB_NAME) as connection:
        insert_info(connection=connection,
                    telegram_id=call.from_user.id,
                    first_name=call.from_user.first_name,
                    last_name=call.from_user.last_name,
                    request=str_info_request,
                    response=str_info_response
                    )


@dp.callback_query_handler(state=States.start)
async def search_options(call: types.CallbackQuery, state: FSMContext):
    await state.update_data({'type': call.data})
    await call.message.answer(f'Твой выбор {type_base[call.data]}, отлично.\nВыбери критерии поиска:',
                              reply_markup=keyboard_client.get_kb_lvl_1())
    await States.lvl_1.set()


@dp.callback_query_handler(state=States.lvl_1)
async def options(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'genres.name':
        await call.message.answer('Поиск по жанрам (содержит до 5 позиций,'
                                  'сохраняются 5 последних выбранных жанров):',
                                  reply_markup=keyboard_client.get_kb_lvl_2())
        await States.lvl_2.set()
    elif call.data == 'rating.imdb':
        await call.message.answer('Поиск по рейтингу IMDB (интервал между выбранными числами, '
                                  'сохраняются последние 2 числа):',
                                  reply_markup=keyboard_client.get_kb_lvl_3())
        await States.lvl_3.set()
    elif call.data == 'year':
        await call.message.answer('Поиск по годам (сохраняется 1 последний выбор):',
                                  reply_markup=keyboard_client.get_kb_lvl_4())
        await States.lvl_4.set()
    elif call.data == 'back_0':
        await call.message.answer('Что будем искать?',
                                  reply_markup=keyboard_client.get_kb_lvl_0())
        await States.start.set()
    elif call.data == 'next_0':
        data = await state.get_data()
        if len(data) == 1:
            await call.message.answer('Ничего не выбрано, пожалуйста выберите минимум 1 критерий поиска:',
                                      reply_markup=keyboard_client.get_kb_lvl_1())
            await States.lvl_1.set()
        else:
            if data.get('rating.imdb') is not None:
                if len(data.get('rating.imdb')) == 2:
                    rating_imdb_str = data['rating.imdb'][0] + '-' + data['rating.imdb'][1]
                    data['rating.imdb'] = rating_imdb_str
                    await state.update_data(data)
                    data = await state.get_data()
            str_type = type_base[data.get('type')]
            list_genres = data.get('genres.name')
            str_genres = ''
            if list_genres is not None:
                for i_genres in list_genres:
                    str_genres = str_genres + i_genres + ' '
            else:
                str_genres = None
            str_rating = data.get('rating.imdb')
            str_year = data.get('year')
            str_info_request = f' Тип: {str_type}|Жанры: {str_genres}|Рейтинг imdb {str_rating}|Релиз: {str_year}'
            result_search = await get_movie(data)
            result = json.loads(result_search.text)
            count = 0
            str_info_response = ''
            for i_movie in result['docs']:
                if count != 10:
                    if i_movie['name'] is not None:
                        name = i_movie['name']
                        length = i_movie.get("movieLength")
                        rating = i_movie.get("rating").get("imdb")
                        date = i_movie.get("year")
                        description = i_movie.get("shortDescription")
                        if length is not None:
                            length_str = f'Продолжительность {length} минут'
                        else:
                            length_str = ''
                        if rating is not None:
                            rating_str = f'Рейтинг IMDb - {rating}'
                        else:
                            rating_str = ''
                        if date is not None:
                            date_str = f'Дата релиза - {date}'
                        else:
                            date_str = ''
                        if description is not None:
                            description_str = f'Краткое описание: {description}'
                        else:
                            description_str = ''
                        photo = ''
                        if i_movie.get("poster") is not None:
                            photo = i_movie["poster"]["url"]
                        await call.message.answer(
                            f'Название - {name}\n'
                            f'{length_str}\n'
                            f'{rating_str}\n'
                            f'{date_str}\n'
                            f'{description_str}\n'
                            f'{photo}'
                        )
                        count += 1
                        str_info_response = str_info_response + \
                                            f'{name}|{length_str}|{rating_str}|{date_str}|{description_str}|{photo}\n'
                else:
                    break
            with create_connection_mysql_db(HOST, USER, PASSWORD, DB_NAME) as connection:
                insert_info(connection=connection,
                            telegram_id=call.from_user.id,
                            first_name=call.from_user.first_name,
                            last_name=call.from_user.last_name,
                            request=str_info_request,
                            response=str_info_response
                            )
            await States.search.set()
    # elif call.data == 'test':
    #     data = await state.get_data()
    #     await call.message.answer(f'{data}')


@dp.callback_query_handler(state=States.lvl_2)
async def search_genres(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if call.data == 'next_1':
        data = await state.get_data()
        if data.get('genres.name') is None or len(data.get('genres.name')) == 0:
            await call.message.answer('Ничего не выбрано, пожалуйста выберите минимум 1 жанр'
                                      ' для поиска или вернитесь назад:',
                                      reply_markup=keyboard_client.get_kb_lvl_2())
        else:
            await call.message.answer('Если требуется выбери дополнительные критерии поиска:',
                                      reply_markup=keyboard_client.get_kb_lvl_1())
            await States.lvl_1.set()
    elif call.data == 'back_1':
        await call.message.answer('Выбери критерии поиска:',
                                  reply_markup=keyboard_client.get_kb_lvl_1())
        await States.lvl_1.set()
    # elif call.data == 'test':
    #     await call.message.answer(f'{data}')
    else:
        if data.get('genres.name') is None:
            await state.update_data({'genres.name': []})
            data = await state.get_data()
        if len(data['genres.name']) < 5:
            data['genres.name'].append(call.data)
        else:
            del data['genres.name'][0]
            data['genres.name'].append(call.data)
        await state.update_data(data)


@dp.callback_query_handler(state=States.lvl_3)
async def search_rating(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if call.data == 'next_1':
        data = await state.get_data()
        if data.get('rating.imdb') is None or len(data.get('rating.imdb')) == 0:
            await call.message.answer('Ничего не выбрано, пожалуйста выберите минимум 1 оценку рейтинга'
                                      ' для поиска или вернитесь назад:',
                                      reply_markup=keyboard_client.get_kb_lvl_3())
        else:
            await call.message.answer('Если требуется выбери дополнительные критерии поиска:',
                                      reply_markup=keyboard_client.get_kb_lvl_1())
            await States.lvl_1.set()
    elif call.data == 'back_1':
        await call.message.answer('Выбери критерии поиска:',
                                  reply_markup=keyboard_client.get_kb_lvl_1())
        await States.lvl_1.set()
    # elif call.data == 'test':
    #     await call.message.answer(f'{data}')
    else:
        if data.get('rating.imdb') is None:
            await state.update_data({'rating.imdb': []})
            data = await state.get_data()
        if len(data['rating.imdb']) < 2:
            data['rating.imdb'].append(call.data)
        else:
            del data['rating.imdb'][0]
            data['rating.imdb'].append(call.data)
        await state.update_data(data)


@dp.callback_query_handler(state=States.lvl_4)
async def search_year(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if call.data == 'next_1':
        if data.get('year') is None or len(data.get('year')) == 0:
            await call.message.answer('Ничего не выбрано, пожалуйста выберите год релиза '
                                      'для поиска или вернитесь назад:',
                                      reply_markup=keyboard_client.get_kb_lvl_3())
        else:
            await call.message.answer('Если требуется выбери дополнительные критерии поиска:',
                                      reply_markup=keyboard_client.get_kb_lvl_1())
            await States.lvl_1.set()
    elif call.data == 'back_1':
        await call.message.answer('Выбери критерии поиска:',
                                  reply_markup=keyboard_client.get_kb_lvl_1())
        await States.lvl_1.set()
    # elif call.data == 'test':
    #     await call.message.answer(f'{data}')
    else:
        # if data.get('year') is None:
        #     await state.update_data({'year': []})
        #     data = await state.get_data()
        # if len(data['year']) == 0:
        #     data['year'].append(call.data)
        # else:
        #     del data['year'][0]
        #     data['year'].append(call.data)
        data['year'] = call.data
        await state.update_data(data)
