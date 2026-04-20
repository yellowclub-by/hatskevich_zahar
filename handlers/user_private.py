from aiogram import types, Router , F
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
    await message.answer('решатель задач по физике')


@user_router.message(Command('gdz'))
async def gdz(message: types.message):
    await message.answer('ссылко')


@user_router.message(Command('FizikAi'))
async def Ai(message: types.message):
    await message.answer('Режим Физика')


@user_router.message(Command('zadacha'))
async def zadacha(message: types.message):
    await message.answer('Крутая задача от физика')


@user_router.message(Command('theme'))
async def theme(message: types.message):
    await message.answer('пиши свою тему')

#@user_router.message(F.text)#filter text
#@user_router.message(F.image == 'физик')#filter image
#@user_router.message(F.text == 'физик')#filter texta
#@user_router.message(F.text.lower()== "физик")#filter lower
#@user_router.message(F.text.lower().contains("fizik"))#filter контейнер
#@user_router.message(F.text.lower().endwith("?"))#filter заканчивается на
# @user_router.message(F.text.lower().endswith("?"))
@user_router.message(F.text.lower().startswith("ты"))
async def echo(message: types.Message):
    await message.answer('да')

