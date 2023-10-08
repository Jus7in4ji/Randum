from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler,MessageHandler, filters
import openai

openai.api_key = "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"

bot_token="6258650807:AAGnFD_kYOGTHHhg30_qSDQGi9i7g0BCGgo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.sendMessage(
        text = "welcome to telegram bot powered by OPENAI",
        chat_id = update.effective_chat.id
    )
async def image (update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = ' '.join(context.args)

    img = openai.Image.create(
        prompt= text,
        size= "1024x1024",
        n=1   
    )
    
    img_url = img.data[0].url

    await context.bot.sendPhoto(
        photo = img_url,
        chat_id = update.effective_chat.id
    )

async def telljoke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.sendMessage(
        text = "your existence :/",
        chat_id = update.effective_chat.id
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.sendMessage(
        text = update.effective_message.text,

        chat_id = update.effective_chat.id
    )

if __name__=="__main__":
    app = ApplicationBuilder().token(bot_token).build()

    start_handler = CommandHandler("start",start)
    image_handler = CommandHandler("image",image)
    telljoke_handler = CommandHandler("telljoke",telljoke)
    echo_handler = MessageHandler(
        filters.TEXT &(~filters.COMMAND),
        echo
        )

    app.add_handler(start_handler)
    app.add_handler(image_handler)
    app.add_handler(echo_handler)
    app.add_handler(telljoke_handler)
    app.run_polling()