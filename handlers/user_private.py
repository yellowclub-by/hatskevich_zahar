from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile
from keyboards import reply, inline

user_router = Router()


# Я жирный физик и помогу тебе с заданиями такими как
# 1.гДЗ-/gdz
# 2.физик включает ИИ мод-/fizik
# 3.Крутые задачи для физиков-ядерщиков-/zadacha
# 4.Помощь с темой-/theme
# 5.Инфо о боте-/info

@user_router.message(CommandStart())
async def stat_cmd(message: types.message):
    photo = FSInputFile("fizik/fisiks.jpg")
    await message.answer_photo(photo, caption="""info - 
    /gdz
    /ai
    /intellekt
    /theme""", reply_markup=reply.start_kb)


@user_router.message(F.text.lower().contains("задач"))
@user_router.message(F.text.lower() == 'задач')
@user_router.message(Command('intellekt'))
async def zadacha(message: types.message):
    await message.answer('<b>решатель задач по физике</b>', parse_mode="HTML")


@user_router.message(F.text.lower().contains("гдз"))
@user_router.message(F.text.lower() == 'гдз')
@user_router.message(Command('gdz'))
async def gdz(message: types.message):
    await message.answer('ссылко', reply_markup=reply.fizik_kb, parse_mode="HTML")


@user_router.message(F.text.lower().contains("ии"))
@user_router.message(F.text.lower() == 'ии')
@user_router.message(Command('ai'))
async def Ai(message: types.message):
    await message.answer('Режим Физика', reply_markup=inline.inline_kb)


@user_router.message(F.text.lower().contains('интеллект'))
@user_router.message(F.text.lower() == 'интеллект')
@user_router.message(Command('intellekt'))
async def krytayazadacha(message: types.message):
    await message.answer('Крутая задача от физика',reply_markup=inline.inline_kb)


@user_router.message(F.text.lower().contains("тем"))
@user_router.message(F.text.lower() == 'тема')
@user_router.message(Command('theme'))
async def theme(message: types.message):
    await message.answer('пиши свою тему')


# @user_router.message(F.text)#filter text
# @user_router.message(F.image == 'физик')#filter image
# @user_router.message(F.text == 'физик')#filter texta
# @user_router.message(F.text.lower()== "физик")#filter lower
# @user_router.message(F.text.lower().contains("fizik"))#filter контейнер
# @user_router.message(F.text.lower().endwith("?"))#filter заканчивается на
# @user_router.message(F.text.lower().endswith("?"))
@user_router.message(F.text.lower().contains("ты"))
async def echo(message: types.Message):
    await message.answer('да')
    return
