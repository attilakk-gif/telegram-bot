from telegram.ext import Updater, MessageHandler, Filters
import os

TOKEN = os.getenv("TOKEN")

PAROLA_CHIAVE = "shushku"
RISPOSTA = "Zitto! Qui la gente mi conosce!"

def ascolta(update, context):
    if update.message and update.message.text:
        testo = update.message.text.lower()
        if PAROLA_CHIAVE in testo:
            update.message.reply_text(RISPOSTA)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, ascolta))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
