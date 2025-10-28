from aiogram import Router
from aiogram.filters import CommandStart

from . import auth
from states import SignUp


message_router = Router()
message_router.message.register(auth.start_common_answer, CommandStart())
message_router.message.register(auth.start_phone_answer, SignUp.phone)
