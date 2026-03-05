from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

TOKEN = os.environ["TOKEN"]

async def anti_manito(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.reaction:
        for r in update.message.reaction:
            if r.emoji == "👍":
                await update.effective_chat.send_message("SIN MANITOOO 🪚")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, anti_manito))
app.run_polling()
