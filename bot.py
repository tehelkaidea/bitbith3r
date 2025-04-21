from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

BOT_TOKEN = "7656172664:AAHB1sXfvZ_CiIJuXqmh5jEEAslb5QO1Z0U"
START_IMAGE_URL = "https://i.postimg.cc/0j1X0LLk/P2-SOMSA3-X5-KD5-II5-O2-CWSVYD74.jpg"  # Tested direct image URL
BUTTON_URL = "https://bitminer.h3r.fun/"
GROUP_ID = -1002515749152

START_TEXT = """𝗛𝗲𝘆 𝘁𝗵𝗲𝗿𝗲, 𝗳𝘂𝘁𝘂𝗿𝗲 𝗺𝗶𝗻𝗲𝗿!
𝗟𝗼𝗼𝗸𝗶𝗻𝗴 𝗳𝗼𝗿 𝗮 𝘄𝗮𝘆 𝘁𝗼 𝗲𝗮𝗿𝗻 𝗳𝗿𝗲𝗲 𝗺𝗶𝗻𝗶𝗻𝗴 𝗿𝗲𝘄𝗮𝗿𝗱𝘀 𝗲𝗳𝗳𝗼𝗿𝘁𝗹𝗲𝘀𝘀𝗹𝘆?
𝗬𝗼𝘂'𝗿𝗲 𝗶𝗻 𝘁𝗵𝗲 𝗿𝗶𝗴𝗵𝘁 𝗽𝗹𝗮𝗰𝗲!
𝗝𝗼𝗶𝗻 𝗕𝗶𝘁𝗠𝗶𝗻𝗲𝗿 𝘁𝗼𝗱𝗮𝘆 𝗮𝗻𝗱 𝘀𝘁𝗮𝗿𝘁 𝗺𝗶𝗻𝗶𝗻𝗴 𝘄𝗶𝘁𝗵𝗼𝘂𝘁 𝗮𝗻𝘆 𝗶𝗻𝘃𝗲𝘀𝘁𝗺𝗲𝗻𝘁.
𝗜𝘁’𝘀 𝗳𝗮𝘀𝘁, 𝘀𝗶𝗺𝗽𝗹𝗲, 𝗮𝗻𝗱 𝗮𝗯𝘀𝗼𝗹𝘂𝘁𝗲𝗹𝘆 𝗳𝗿𝗲𝗲!
"""

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = f"@{user.username}" if user.username else user.full_name

    keyboard = [[InlineKeyboardButton("🚀 Start Mining", url=BUTTON_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo=START_IMAGE_URL,
        caption=START_TEXT,
        reply_markup=reply_markup
    )

    await context.bot.send_message(chat_id=GROUP_ID, text=f"👤 New User Started Bot: {username}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
