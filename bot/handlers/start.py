from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Привет! Я Arbitr Subscribe.\n"
        "Пока что это каркас проекта.\n"
        "Дальше добавим команды для дел и подписок."
    )
