from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from db.base import AsyncSessionLocal
from db.models import Case

router = Router()


@router.message(Command("cases"))
async def show_cases(message: Message):
    await message.answer("📋 Ваши дела — пока пусто.\n\nОтправьте номер дела, например:\n`А40-123456/2025`")


@router.message(F.text.regexp(r'^[А-Я]\d{2}-\d+/\d{4}$'))
async def handle_case_number(message: Message):
    case_number = message.text.strip().upper()

    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Case).where(Case.case_number == case_number)
        )
        case = result.scalar_one_or_none()

        if not case:
            case = Case(
                case_number=case_number,
                status="В производстве",
            )
            session.add(case)
            try:
                await session.commit()
                await message.answer(
                    f"✅ Дело **{case_number}** создано.\n\n"
                    "Хотите подписаться на обновления?",
                    parse_mode="Markdown",
                )
            except IntegrityError:
                await session.rollback()
                await message.answer("✅ Дело уже существует в базе.")
        else:
            await message.answer(f"✅ Дело **{case_number}** уже есть в базе.")
