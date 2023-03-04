import requests
from config import TOKEN_API


async def get_movie(params: dict) -> requests.models.Response:
    headers = {'X-API-KEY': TOKEN_API,
               'accept': 'application/json'}
    response = requests.get('https://api.kinopoisk.dev/v1/movie?selectFields=name%20movieLength%20rating.imdb%20year'
                            '%20shortDescription%20poster.url&sortField=rating.imdb&sortType=-1&page=1&limit=150',
                            headers=headers,
                            params=params)
    return response


async def get_random_movie(params: dict) -> requests.models.Response:
    headers = {'X-API-KEY': TOKEN_API,
               'accept': 'application/json'}
    response = requests.get('https://api.kinopoisk.dev/v1/movie?selectFields=name%20movieLength%20rating.imdb%20year%20'
                            'shortDescription%20poster.url&page=1&limit=150',
                            headers=headers,
                            params=params)
    return response