import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Token-ро аз Render мегирем, дар ин ҷо намевисем
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(f'Салом {user_name}! 👋\nБоти ман дар Render кор мекунад ✅\n\nФармонҳо:\n/start - Оғоз')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Ин боти аввалини ман аст 😄\nТанҳо /start кор мекунад ҳозир')

if __name__ == '__main__':
    print("✅ Bot started...")
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    
    app.run_polling()
