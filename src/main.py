import logging
import sys
import config
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from src.handlers.famous_people import router as famous_people_router
from src.handlers.common import router as common_router
from src.handlers.coreer_choice import router as coreer_choice_router
from src.handlers.random_facts import router as random_facts_router
from src.handlers.quiz import router as quiz_router
from src.handlers.handler_weather_ai import router as weather_router


async def main() -> None:

    TOKEN = config.token

    dp = Dispatcher()

    dp.include_router(router= weather_router)

    dp.include_router(router= famous_people_router)

    dp.include_router(router= coreer_choice_router)

    dp.include_router(router= random_facts_router)

    dp.include_router(router= quiz_router)

    dp.include_router(router=common_router)

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    await dp.start_polling(bot)


if __name__ == "__main__":
        asyncio.run(main())

