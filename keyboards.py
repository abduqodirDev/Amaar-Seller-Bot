from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


phone_keyboard = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="📱 Telefon raqamni yuborish", request_contact=True)]
        ],
        resize_keyboard=True
)

main_menu = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="ℹ️ Bot haqida")],
            [KeyboardButton(text="👤 Mening ma'lumotlarim")]
        ],
        resize_keyboard=True
)
