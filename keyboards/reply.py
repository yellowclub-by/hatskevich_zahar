from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='zadacha')],
        [KeyboardButton(text='gdz')],
        [KeyboardButton(text='FizikAi'), KeyboardButton(text='krytayazadacha')],
        [KeyboardButton(text='theme')]
    ]
)
