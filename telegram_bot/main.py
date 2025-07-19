import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Logging Setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# START Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Team CSB Downloader Bot!\n\n"
        "✅ Paste any YouTube, Facebook, Drive or Terabox link below.\n"
        "I'll redirect you to the correct download site instantly!"
    )

# Handle Link Message
async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()

    if any(site in url for site in ["youtube.com", "youtu.be"]):
        redirect = f"https://loader.vercel.app/download.html?url={url}"
    elif "facebook.com" in url:
        redirect = f"https://loader.vercel.app/download.html?url={url}"
    elif "drive.google.com" in url:
        redirect = f"https://loader.vercel.app/download.html?url={url}"
    elif "terabox.com" in url or "1024tera.com" in url:
        redirect = f"https://loader.vercel.app/download.html?url={url}"
    else:
        redirect = "❌ Invalid link or unsupported platform."

    await update.message.reply_text(redirect)

# Main Function
if __name__ == '__main__':
    TOKEN = "7995505490:AAH2aXacXAS_7aFyILPjYvTdi_HduybmO7A"

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))

    app.run_polling()
