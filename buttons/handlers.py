from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery, KeyboardButton
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

user_router = Router()


# @user_router.message(F.text == __('Change language'))
# async def change_language(message: Message) -> None:
#     ikb = InlineKeyboardBuilder()
#     ikb.row(InlineKeyboardButton(text=_('🇺🇿uzbek'), callback_data='lang_uz'),
#             InlineKeyboardButton(text=_('🇷🇺russion'), callback_data='lang_ru'))
#     await message.answer(_('Change language'), reply_markup=ikb.as_markup())


@user_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        """
        Здравствуйте! 🌟 Давайте для начала выберем язык обслуживания! \n
Assalomu aleykum! 🌟 Keling, avvaliga xizmat ko’rsatish tilini tanlab olaylik. 🌐 \n
Choose a language, please
        """)


@user_router.message(F.text == __('Change language'))
async def change_language(message: Message) -> None:
    ikb = InlineKeyboardBuilder()
    ikb.row(InlineKeyboardButton(text=_('🇺🇿uzbek'), callback_data='lang_uz'),
            InlineKeyboardButton(text=_('🇷🇺russion'), callback_data='lang_ru'))
    await message.answer(_('Change language'), reply_markup=ikb.as_markup())
