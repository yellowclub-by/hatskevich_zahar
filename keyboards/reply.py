from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='задача')],
        [KeyboardButton(text='гдз')],
        [KeyboardButton(text='ИИ'), KeyboardButton(text='интеллект')],
        [KeyboardButton(text='тема')]
    ],resize_keyboard=True,input_field_placeholder='большой физик'
)
fizik_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='7'), KeyboardButton(text='8'), KeyboardButton(text='9')],
        [KeyboardButton(text='11'), KeyboardButton(text='10')],
    ],resize_keyboard=True
)
