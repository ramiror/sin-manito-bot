from telegram import Update
from telegram.ext import ApplicationBuilder, MessageReactionHandler, ContextTypes
import os

TOKEN = os.environ["TOKEN"]

async def anti_manito(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for r in update.message_reaction.new_reaction:
        if r.emoji == "👍":
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="SIN MANITOOO 🪚"
            )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageReactionHandler(anti_manito))
app.run_polling(allowed_updates=["message_reaction"])
