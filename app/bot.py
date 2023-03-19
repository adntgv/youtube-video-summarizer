from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from os import getenv 
from summarizer import Summarizer
from transcriber import Transcriber

class Bot(): 
    async def summary(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        try:
            partAfterV = update.message.text.split("?v=")[1] 
            id = partAfterV.split("&")[0]
            print("transcribe")
            await update.message.reply_text(text="Transcribing...")
            transcription = await Transcriber().youtube_transcribe(id)
            print("summarize")
            await update.message.reply_text(text="Summarizing...")
            summary = Summarizer().transcription_summarize(transcription, "html")
            print("respond")
            await update.message.reply_text(text=summary)
        except Exception as e:
            print(e)
            await update.message.reply_text(text="Error")

    async def bot_tele(self, text):
        # Create application
        print("Create app")
        application = (
            Application.builder().token(getenv("TELEGRAM_TOKEN")).build()
        )

        # Add handlers
        print("Create handlers")
        application.add_handler(CommandHandler("summary", self.summary))

        # Start application
        await application.bot.set_webhook(url=getenv("TELEGRAM_WEBHOOK"))
        print("Update queue")
        await application.update_queue.put(
            Update.de_json(data=text, bot=application.bot)
        )

        print("application.start")
        async with application:
            await application.start()
            await application.stop()
