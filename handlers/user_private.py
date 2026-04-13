from aiogram import types, Router
from aiogram.filters import CommandStart, Command

user_router = Router()


# Я жирный физик и помогу тебе с заданиями такими как
# 1.гДЗ-/gdz
# 2.физик включает ИИ-ЛГБТ мод-/fizik
# 3.Крутые задачи для физиков-ядерщиков-/zadacha
# 4.Помощь с темой-/theme
# 5.Инфо о боте-/info

@user_router.message(CommandStart())
async def stat_cmd(message: types.message):
    await message.answer(
        """dfghj
        /info - jfsldkjfskd""")


@user_router.message(Command('info'))
async def info(message: types.message):
    await message.answer('Я огромный жирный 2д физик решающий тебе задачи и так же могу быть ИИ-ЛГБТ монстром')


@user_router.message(Command('gdz'))
async def gdz(message: types.message):
    await message.answer('ссылко')


@user_router.message(Command('FizikAi'))
async def Ai(message: types.message):
    await message.answer('Режим Лгбт Физика')


@user_router.message(Command('zadacha'))
async def zadacha(message: types.message):
    await message.answer('Крутая задача от физика')


@user_router.message(Command('theme'))
async def theme(message: types.message):
    await message.answer('пиши свою глупую тему')
