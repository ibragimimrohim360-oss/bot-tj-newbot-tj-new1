import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("8870950829:AAHrviexyWuaO1HFMH-zorVmecEAsWvfO8o")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(f'Салом {user_name}! 👋\nБоти ман дар Render кор мекунад ✅\n\nФармонҳо:\n/start - Оғоз')

if __name__ == '__main__':
    print("✅ Bot started on Render...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
