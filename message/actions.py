import requests
from aiogram.types import Message

from config import BACKEND_URL


async def bot_info(message: Message):
    text = (
        "🤖 <b>Amaar Seller Bot</b>\n\n"
        "Bu bot sizga yangi buyurtmalar haqida avtomatik xabar yuboradi 📦\n"
        "Har bir buyurtma uchun sizga quyidagilar yuboriladi:\n"
        "• 🆔 Buyurtma raqami\n"
        "• 💰 Umumiy summa\n"
        "• 👤 Xaridor ma’lumotlari"
    )
    await message.answer(text, parse_mode="HTML")


async def seller_info(message: Message):
    response = requests.get(f"{BACKEND_URL}/seller-info/{message.from_user.id}/")
    data = response.json()

    if data.get("detail") == "Error":
        return

    # Ma’lumotlar
    name = data.get("name", data.get("full_name"))
    phone = data.get("phone", data.get("phone"))
    # balance = data.get("balance", "0 so‘m")
    status = data.get("status", "faol")

    text = (
        "👤 <b>Sizning ma’lumotlaringiz</b>\n\n"
        f"🧾 Ism: {name}\n"
        f"📱 Telefon: {phone}\n"
        # f"💰 Balans: {balance}\n"
        f"📊 Status: {status}\n\n"
        "Agar ma’lumotlar noto‘g‘ri bo‘lsa, support bilan bog‘laning: @amaar_support_bot"
    )

    await message.answer(text, parse_mode="HTML")
