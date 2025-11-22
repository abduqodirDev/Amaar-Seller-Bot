import requests

from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from config import  BACKEND_URL
from states import SignUp
from keyboards import phone_keyboard, main_menu


async def start_common_answer(message: Message, state: FSMContext):
    if message.from_user.id == 1028459910:
        text = (
            "Salom! Siz Abduqodir Do'stmurodov Amaar MarketPlace’da bosh dasturchisiz. 👋\n"
            "Yangi buyurtmalar haqida shu bot orqali sizni xabardor qilib turamiz."
        )
        await message.answer(text)
    elif message.from_user.id == 7780293305:
        text = (
            "Salom! Siz Furqat Yaqubov Amaar MarketPlace egasisiz. 👋\n"
            "Yangi buyurtmalar haqida shu bot orqali sizni xabardor qilib turamiz."
        )
        await message.answer(text)

    elif message.from_user.id == 6681446615:
        text = (
            "Salom! Siz Laziz Omonov Amaar MarketPlace marketologisiz. 👋\n"
            "Yangi buyurtmalar haqida shu bot orqali sizni xabardor qilib turamiz."
        )
        await message.answer(text)

    elif message.from_user.id == 5803698389:
        text = (
            "Salom! Siz Nurbek Rasulov Amaar MarketPlace'da bosh dasturchisiz. 👋\n"
            "Yangi buyurtmalar haqida shu bot orqali sizni xabardor qilib turamiz."
        )
        await message.answer(text)

    else:
        response = requests.post(f"{BACKEND_URL}/check-user/", data={"telegram_id": message.from_user.id})
        data = response.json()
        if data['result']:
            text = (
                f"👋 Salom, <b>{message.from_user.first_name}</b>!\n\n"
                "Sizning akkauntingiz allaqachon <b>Amaar Seller</b> tizimiga ulangan ✅\n\n"
                "Endi siz yangi buyurtmalar haqidagi xabarlarni shu yerda olasiz.\n\n"
            )
            await message.answer(text, reply_markup=main_menu, parse_mode='HTML')
        else:
            text = (
                "🛍️ <b>Amaar Marketplace</b>’ga xush kelibsiz!\n\n"
                "📦 Biz sizga yangi buyurtmalar haqida tezkor bildirishnomalar yuboramiz.\n\n"
                "Iltimos, quyidagi tugma orqali telefon raqamingizni ulab qo‘ying 👇"
            )
            await message.answer(text, reply_markup=phone_keyboard, parse_mode='HTML')
            await state.set_state(SignUp.phone)


async def start_phone_answer(message: Message, state: FSMContext):
    if message.contact:
        request_data = {
            "phone": message.contact.phone_number,
            "telegram_id": message.from_user.id
        }

        response = requests.post(f"{BACKEND_URL}/check-seller/", data=request_data)
        data = response.json()
        result = data.get('result')
        if result == "success":
            text = (
                "🎉 <b>Tabriklaymiz!</b>\n\n"
                "Siz tizimga muvaffaqiyatli ulanib, sotuvchi sifatida faollashtirildingiz ✅\n\n"
                "Quyidagi bo‘limlardan birini tanlang 👇"
            )
            await message.answer(text, reply_markup=main_menu, parse_mode='HTML')

        elif result == "process":
            text = (
                "⏳ Sizning ro‘yxatdan o‘tish jarayoningiz hali to‘liq yakunlanmagan.\n\n"
                "🧾 Administrator tomonidan tasdiqlangandan so‘ng bot avtomatik faollashadi.\n"
                "Iltimos, biroz kuting yoki support bilan bog‘laning."
            )
            await message.answer(text, reply_markup=ReplyKeyboardRemove(), parse_mode='HTML')

        elif result == "None":
            text = (
                "🚫 Sizning raqamingiz <b>Amaar Marketplace</b> sotuvchilari ro‘yxatida topilmadi.\n\n"
                "Agar bu xato deb o‘ylasangiz, iltimos, "
                "<b>@amaar_support_bot</b> bilan bog‘laning 🧑‍💻"
            )
            await message.answer(text, reply_markup=ReplyKeyboardRemove(), parse_mode='HTML')

        await state.clear()
