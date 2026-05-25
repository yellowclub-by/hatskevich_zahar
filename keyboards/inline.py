from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='fiziks', callback_data='fiziks_btn')],
        [InlineKeyboardButton(text='Dominate', callback_data='Dominate_btn')],
        [InlineKeyboardButton(text='SmartGay', callback_data='SmartGay_btn')],
    ]
)
