from aiogram import Router, F
from aiogram.filters import CommandStart

from . import auth
from . import actions
from states import SignUp


message_router = Router()
message_router.message.register(auth.start_common_answer, CommandStart())
message_router.message.register(auth.start_phone_answer, SignUp.phone)
message_router.message.register(actions.bot_info, F.text == "ℹ️ Bot haqida")
message_router.message.register(actions.seller_info, F.text == "👤 Mening ma'lumotlarim")
