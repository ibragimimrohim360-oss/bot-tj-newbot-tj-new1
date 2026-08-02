import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.getenv("8870950829:AAHrviexyWuaO1HFMH-zorVmecEAsWvfO8o")

def start(update, context):
    update.message.reply_text('Салом! Бот дар Render кор мекунад ✅')

def main():
    print("✅ Bot started on Render...")
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
