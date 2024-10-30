from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from filters import IsAdmin
from run.config import ADMIN_LIST

admin_router = Router()


@admin_router.message(CommandStart, IsAdmin(ADMIN_LIST))
async def admin_start(message: Message):
    btn = [
        [KeyboardButton(text="Salom")]
    ]
    rkb = ReplyKeyboardBuilder(btn)
    rkb.adjust(2)
    await message.answer('Welcome! Choose. You is admin', reply_markup=rkb.as_markup(resize_keyboard=True))
