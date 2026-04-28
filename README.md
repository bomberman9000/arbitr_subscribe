# Arbitr Subscribe

Telegram-бот + Obsidian для отслеживания арбитражных дел.

## Запуск

```bash
cp .env.example .env
# Добавь BOT_TOKEN в .env

docker-compose up -d --build
```

## Структура

- `bot/` — Telegram-бот (aiogram 3)
- `db/` — SQLAlchemy модели
- `sync_obsidian/` — синхронизация в Obsidian
