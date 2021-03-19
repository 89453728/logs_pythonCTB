import telegram
from telegram.ext import *
import time

token = "1625126519:AAGnz_ptXJXn21Nz7zPoNFR_LAhiQfYXruY"
repeat = False

def dani (update: Updater, context: CallbackContext) -> None:
    update.message.reply_text("con que dani eh!!, preparate para sufrir el reglazo de acero!!")

def msg (update: Updater, context: CallbackContext):
    chat_id = update.message.chat.id
    chat_type = update.message.chat.type
    text = update.message.text


    if (text[0:4] == "calc" or text[0:4] == "Calc"):
        update.message.reply_text(eval(text[5:]))
    elif(text[0:6] == "script" or text[0:6] == "Script"):
        update.message.reply_text(exec(text[7:]))
    
def main ():
    updater = Updater(token, use_context = True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("me_llamo_dani",dani))

    dispatcher.add_handler(MessageHandler(Filters.text | Filters.photo, msg))

    updater.start_polling(clean = True) # limpiar mensajes anteriores a la activacion
    updater.idle()

if __name__ == "__main__":
    main()



# estructura de un JSON de un mensaje de la api en api.JSON