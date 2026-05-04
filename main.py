from aiogram import Bot, Dispatcher, types , F
import asyncio
from handlers.user_private import user_router
from handlers.user_group import group_router
bot = Bot(token='8691719670:AAGn8fYaRQH55MIfH6Y2cTcANmmiXi4gw_g')
dp = Dispatcher()
dp.include_router(user_router)
dp.include_router(group_router)

async def main():
    print("fizik")
    await dp.start_polling(bot)


asyncio.run(main())
