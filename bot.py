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
    ],
    "cordoni": [
        "Oh ma sei matto?",
        "Vado a letto",
        "nino?",
        "c'è 20 euro",
        "non c'ho una lira",
        "questa settimana non posso bere",
        "ho l'allergia",
        "questa settimana non posso mangiare",
        "mi fa male la pancia",
        "sei matto?? sono vecchio",
        "ho 13 anni",
        "ho 22 anni",
        "sono del '98",
        "sono un 2003",
        "mia mamma è svedese",
        "mia mamma è francese",
        "mia mamma è brasiliana",
    ],
    

     "nico": [
        "ci sto! sono dentro",
        "Oh ma te sei scemo",
        "il mio Spezia",
        "ma voi state male",
        "buonasera dottore",
        "quella è la porta",
         "sono il miglior barista di Cascina",
         "Wimo è il miglior locale del mondo",
         "Missiva? (poi non esce)",
         "Fortnite?",
         "sono la miglior cosa che vi poteva succedere",
         "sono povero",
         "eehhhvv amico mio",
         "no qui non lo fai",
         " 🐵 "
    ],
    "prova": [
        " 🐵 "
    ],
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

