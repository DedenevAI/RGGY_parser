import asyncio
from aiogram import Bot, Dispatcher
from aiogram import html
from handlers import menu_selectors

TOKEN = "6915376896:AAGKI2FImWnFlw9-uwV2fZAWbnK5QoILupQ"


async def main():
    bot = Bot(token=TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(menu_selectors.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
