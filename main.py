from environ import Env

from aiogram import Dispatcher, Bot
from asyncio import run

from message import message_router


dp = Dispatcher()
env = Env()
Env.read_env('.env')

bot_token = env("BOT_TOKEN")
BACKEND_URL = env("BACKEND_URL")


async def startup_answer(bot: Bot):
    await bot.send_message(1028459910, "Bot ishga tushdi! ✔")


async def shutdown_answer(bot: Bot):
    await bot.send_message(1028459910, "Bot ishdan to'xtadi! :(")


async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)

    dp.include_router(message_router)
    # dp.include_router(callback_router)

    bot = Bot(bot_token)
    await dp.start_polling(bot, polling_timeout=0)

run(start())
