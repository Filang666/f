import asyncio
from create_bot import bot, dp
from handlers.start import start_router
from parsing1 import pars
from pdftoimage import converter
from imageedit import startedit

# from work_time.time_func import send_time_msg

async def main():
    # scheduler.add_job(send_time_msg, 'interval', seconds=10)
    # scheduler.start()
    pars()
    converter()
    startedit()
    dp.include_router(start_router)
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())