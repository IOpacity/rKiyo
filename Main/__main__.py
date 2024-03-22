from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes, CommandHandler

from Main.utils.decorators import kiyocmd

import time
from . import application, LOGS, start_time

txt = '''
Hey *{}*!, 
I'm *{}* An Unofficial Ex Girlfriend of @CustomUser.

I'm here to assist you and make your chat experience enjoyable! 
Click Help button to find out more about how to use me to my full potential.
━━━━━━━━━━━━━━━━━━━━━━━━
⋟ **Uptime:** 

If you have any questions, need assistance with something, or just want to have a friendly chat, don't hesitate to reach out.
'''

def get_readable_time(seconds: int) -> str:
    intervals = [('days', 86400), ('h', 3600), ('m', 60), ('s', 1)]
    time_string = ''
    for name, count in intervals:
        value = seconds // count
        if value > 0:
            seconds -= value * count
            time_string += f'{value}{name}'

    return time_string

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type == "private":
        await update.effective_message.reply_video(
            video='https://i.imgur.com/BHZ1DPK.mp4', 
            caption=txt.format(update.effective_user.first_name, context.bot.first_name),
            parse_mode=ParseMode.MARKDOWN
        )
    else:
        await update.effective_message.reply_text(f"Hi, I'm {context.bot.first_name}\nuptime: {get_readable_time(time.time() - start_time)}")

def main():
    LOGS.info('Successfully started!')
    application.add_handler(CommandHandler('start', start))
    application.run_polling()

if __name__ == '__main__':
    main()
    