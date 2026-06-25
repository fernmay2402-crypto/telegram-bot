from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🌐 สมัครสมาชิก", url="https://www.time2lucky.com/users/home/index/4LmA4Lif4Li04Lij4LmM?type=register&openExternalBrowser=1")],
        [InlineKeyboardButton("💬 ติดต่อแอดมิน", url="https://lin.ee/rL3uLnc")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 ยินดีต้อนรับ\n\nกดปุ่มด้านล่างเพื่อเริ่มใช้งาน",
        reply_markup=reply_markup
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
