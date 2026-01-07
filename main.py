import os
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

keyboard = [
    ["Кружок", "Помощь"]
]

reply_keyboard = ReplyKeyboardMarkup(keyboard, True, False)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет, я - бот! Что вы хотите сделать?", reply_markup=reply_keyboard)

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    file_id = os.getenv("FILE_ID")

    if text == "Кружок":
        await update.message.reply_video_note(file_id, reply_markup=reply_keyboard)
    elif text == "Помощь":
        await update.message.reply_text("Тут должна была быть помощь...", reply_markup=reply_keyboard)
    else:
        await update.message.reply_text("Я пока не совсем понимаю такие промпты...", reply_markup=reply_keyboard)

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv("TOKEN_ID")).build()
    
    start_handler = CommandHandler('start', start)
    keyboard_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, buttons)

    application.add_handler(start_handler)
    application.add_handler(keyboard_handler)
    
    application.run_polling()