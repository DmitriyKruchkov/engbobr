import asyncio
from core import dp, bot
from routes import router

dp.include_router(router=router)


async def main():
    await dp.start_polling(bot)
    try:
        await asyncio.Future()
    except BaseException as e:
        print(e)


if __name__ == '__main__':
    asyncio.run(main())
