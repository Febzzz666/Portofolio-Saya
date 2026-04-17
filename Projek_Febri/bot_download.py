from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import requests

TOKEN = "8336798678:AAGpyboXCs5o42kVxFp87QYPheMF2YeyYyE"

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Kirim link file, nanti Febri bantu downloadkan 🤖"
    )

# fungsi download file
def download_file(url, filename):
    r = requests.get(url)
    open(filename, 'wb').write(r.content)

# handle pesan (link)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text

    try:
        filename = url.split("/")[-1]

        download_file(url, filename)

        await update.message.reply_text("Download selesai ✅")

        # kirim file ke user
        await update.message.reply_document(document=open(filename, "rb"))

    except:
        await update.message.reply_text("Gagal download ❌ pastikan link benar")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot jalan...")
app.run_polling()