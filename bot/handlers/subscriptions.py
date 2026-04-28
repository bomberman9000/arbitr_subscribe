from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("subscriptions"))
async def subscriptions(message: Message):
    await message.answer("Раздел подписок (subscriptions) — в разработке.")
