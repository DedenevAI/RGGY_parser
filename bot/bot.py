import asyncio
from aiogram import Bot, Dispatcher
from aiogram import html
from handlers import menu_selectors
from aiogram.fsm.storage.memory import MemoryStorage
import logging

TOKEN = "6915376896:AAGKI2FImWnFlw9-uwV2fZAWbnK5QoILupQ"


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    bot = Bot(token=TOKEN, parse_mode="HTML")
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_routers(menu_selectors.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    