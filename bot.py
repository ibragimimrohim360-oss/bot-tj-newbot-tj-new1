import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("8870950829:AAHrviexyWuaO1HFMH-zorVmecEAsWvfO8o")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Салом! Бот дар Render кор мекунад ✅')

def main():
    print("✅ Bot started...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()
