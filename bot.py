#!/usr/bin/env python3
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    MessageReactionHandler,
    ContextTypes,
    filters,
)

TOKEN = os.environ["TOKEN"]


async def anti_manito_reaction(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mr = update.message_reaction
    if not mr:
        return

    for r in mr.new_reaction:
        if getattr(r, "emoji", None) == "👍":
            await context.bot.send_message(
                chat_id=mr.chat.id,
                text="SIN MANITOOO 🪚",
                reply_to_message_id=mr.message_id,
            )


async def anti_manito_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if not msg or not msg.text:
        return

    text = msg.text.lower()

    if "👍" in msg.text:
        await msg.reply_text("SIN MANITOOO 🪚")

    if "manito" in text:
        await context.bot.set_message_reaction(
            chat_id=msg.chat.id,
            message_id=msg.message_id,
            reaction=["👀"],
        )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageReactionHandler(anti_manito_reaction))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), anti_manito_text))

app.run_polling(allowed_updates=["message", "message_reaction"])
