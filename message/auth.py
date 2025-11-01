import requests

from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from config import  BACKEND_URL
from states import SignUp
from keyboards import phone_keyboard


async def start_common_answer(message: Message, state: FSMContext):
    if message.from_user.id == 1028459910 or message.from_user.id == 7780293305:
        await message.answer("Salom, siz Amaar MarketPlace egasisiz")
    else:
        response = requests.post(f"{BACKEND_URL}/check-user/", data={"telegram_id": message.from_user.id})
        data = response.json()
        if response.status_code == 200 and data['result'] == True:
            await message.answer("Salom siz Amaar marketplace sotuvchisisiz")
        else:
            await message.answer("Iltimos, telefon raqamingizni kiriting.", reply_markup=phone_keyboard)
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
            await message.answer("sotuvchi sifatida muvaffaqiyatli ro'yxatdan o'tdingiz", reply_markup=ReplyKeyboardRemove())
        elif result == "process":
            await message.answer("Siz hali to'liq ro'yxatdan o'tmagansiz", reply_markup=ReplyKeyboardRemove())
        elif result == "None":
            await message.answer("Siz Amaar marketplace sotuvchisi emassiz", reply_markup=ReplyKeyboardRemove())

        await state.clear()
