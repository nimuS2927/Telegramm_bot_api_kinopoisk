from aiogram.utils import executor
from create_bot import dp
from BaseDate import create_db
from handlers import client


if __name__ == '__main__':
    async def on_start_bot(_):
        print('Bot started')
    executor.start_polling(dp, skip_updates=True, on_startup=on_start_bot)