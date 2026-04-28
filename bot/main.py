import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from db.base import engine
from db.models import Base
from bot.handlers.start import router as start_router
from bot.handlers.cases import router as cases_router
from bot.handlers.subscriptions import router as subscriptions_router

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(cases_router)
dp.include_router(subscriptions_router)


async def main():
    # Создаём таблицы
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    print("🚀 Arbitr Subscribe Bot запущен")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
