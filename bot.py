import logging
import os

from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from telegram import Update

from config import TELEGRAM_TOKEN, OUTPUT_DIR
from orchestrator import run_thesis_pipeline

logging.basicConfig(level=logging.INFO)
os.makedirs(OUTPUT_DIR, exist_ok=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أرسل:\n/generate عنوان البحث"
    )

async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text("اكتب عنوان البحث")
        return

    topic = " ".join(context.args)

    msg = await update.message.reply_text(
        "⏳ بدء المعالجة..."
    )

    async def progress(text):
        try:
            await msg.edit_text(text)
        except Exception:
            pass

    try:
        result = await run_thesis_pipeline(topic, progress)

        await context.bot.send_document(
            chat_id=update.effective_chat.id,
            document=open(result["pdf_path"], "rb"),
            filename="research.pdf",
            caption="✅ تم إنشاء البحث بنجاح"
        )

    except Exception as e:
        await update.message.reply_text(f"❌ خطأ:\n{e}")

if __name__ == "__main__":
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("generate", generate))

    print("BOT STARTED")
    app.run_polling()