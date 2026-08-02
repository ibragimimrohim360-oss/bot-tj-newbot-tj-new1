import os
from telegram.ext import Application, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")  # <-- аз Render мегирад, на аз ин ҷо

async def start(update, context):
    await update.message.reply_text('Салом! Ман кор мекунам ✅')

def main():
    print("✅ Bot started...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()
