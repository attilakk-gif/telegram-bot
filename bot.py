from telegram.ext import Updater, MessageHandler, Filters
import os
import random

TOKEN = os.getenv("TOKEN")

# Dizionario TRIGGER → LISTA DI RISPOSTE
TRIGGERS = {
    "shushku": [
        "Zitto! Qui la gente mi conosce!",
        "Oh, abbassa la voce!",
        "Ehi, piano con le parole!",
        "Non farmi fare figuracce!",
        "Zitto! Io con voi non ci esco più",
        "Li c'è il su' ragazzo!"
    ],
    "fabio": [
        "Bocca mia stai zitta!",
        "Ma vatti a fa fa un pompino!",
        "Te sei un bimbettone",
        "Te sei un bimbettone",
        "Boria 100%",
        "Te mi hai suonato il campanello",
        "Ma te sei un depravato",
        "Oh se ride vuol dire che è vero",
        "È un bagascione",
        "Basta un cinquantino",
        "Chi dei due fa l'omo?"
    ]
}

def ascolta(update, context):
    if update.message and update.message.text:
        testo = update.message.text.lower()

        for trigger, risposte in TRIGGERS.items():
            if trigger in testo:
                update.message.reply_text(random.choice(risposte))
                return

        

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, ascolta))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

