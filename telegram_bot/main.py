from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = "7995505490:AAH2aXacXAS_7aFyILPjYvTdi_HduybmO7A"

start_buttons = [
    [InlineKeyboardButton("🎥 YouTube Downloader", url="https://teamcsb.vercel.app/download.html?platform=youtube")],
    [InlineKeyboardButton("📘 Facebook Downloader", url="https://teamcsb.vercel.app/download.html?platform=facebook")],
    [InlineKeyboardButton("📁 Google Drive Downloader", url="https://teamcsb.vercel.app/download.html?platform=drive")],
    [InlineKeyboardButton("📦 Terabox Downloader", url="https://teamcsb.vercel.app/download.html?platform=terabox")],
    [InlineKeyboardButton("🚨 Report Section", url="https://teamcsb.vercel.app/report.html")]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧠 Welcome to Team CSB Downloader Bot!\n\nChoose a platform to start downloading 👇",
        reply_markup=InlineKeyboardMarkup(start_buttons)
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
