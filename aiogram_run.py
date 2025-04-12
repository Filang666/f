import asyncio
from create_bot import bot, dp, scheduler
from handlers.start import start_router
from parsing1 import pars
from pdftoimage import converter
from imageedit import startedit
from chechday import fullcheck
# from work_time.time_func import send_time_msg

async def main():
    # scheduler.add_job(send_time_msg, 'interval', seconds=10)
    # scheduler.start()
    pars()
    converter()
    startedit()
    fullcheck()
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
