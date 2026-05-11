import types

from aiogram import Router,F

group_router = Router()
rejected_words=["лох","плохой","глупый","Мальчуган","Хульганье"]
@group_router.message(F.text)
async def cleaner(message: types.message):
    await message.answer('.''.''.')
    word_list = message.text.split(" ")
    for word in word_list:
        if word.lower() in rejected_words:
            await message.answer(F"{message.from_user.first_name},Сообщение ты 😡😡😡😡 и нарушил правил")
            await message.delete()
            break
