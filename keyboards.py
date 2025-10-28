from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


phone_keyboard = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="Phone number", request_contact=True)]
        ],
        resize_keyboard=True
)
