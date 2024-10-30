import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from aiogram.utils.i18n import I18n, FSMI18nMiddleware

from buttons.admin import admin_router
from buttons.handlers import user_router
from run.config import TOKEN

dp = Dispatcher()
# BOT_TOKEN = "7949581500:AAHfF76zuwZLkIPc63Pmx9WgXjfLw3TCUcc"


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # i18n = I18n(path="locales", default_locale="en", domain="messages")
    # dp.update.outer_middleware(FSMI18nMiddleware(i18n))
    # dp.startup.register(on_startup)
    dp.include_routers(user_router, admin_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
