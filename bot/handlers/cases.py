from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("cases"))
async def cases(message: Message):
    await message.answer("Раздел дел (cases) — в разработке.")
