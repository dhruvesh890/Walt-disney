import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Bot is live and working! Type /help to see available commands.")

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Available commands:\n"
        "/start - Check if bot is running\n"
        "/help - Show this help message"
    )

if __name__ == '__main__':
    BOT_TOKEN = os.getenv("7900927113:AAE7NgOnGpznkIvaJUCQSKZeH5J_ozE8uVM")
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("✅ Bot started... waiting for commands.")
    app.run_polling()
