import requests
import time
import os
import json

payloads = [
    "price: ",
    ""
]

token = "1646568825:AAGV8M7O9WpENt0-AeS8PXBBDoj8MwD8bfg"
chatId = "616166895"

# https://api.telegram.org/bot1646568825:AAGV8M7O9WpENt0-AeS8PXBBDoj8MwD8bfg/sendMessage?chat_id=616166895&parse_mode=Markdown&text=hola
def main():
    message1 = "hola yassin"
    sendMessage(token, chatId, message1)

    r = getMessage(token, 0)
    for i in r:
        try:
            print("==================================================")
            print("NUEVO MENSAJE")
            print("id del mensaje: " + str(i["message"]["message_id"]))
            print("id del chat: " + str(i["message"]["chat"]["id"]))
            print("texto del mensaje: " + i["message"]["text"])
        except:
            print("==================================================")
            print("MENSAJE EDITADO")
            print("id del mensaje: " + str(i["edited_message"]["message_id"]))
            print("id del chat: " + str(i["edited_message"]["chat"]["id"]))
            print("texto del mensaje: " + i["edited_message"]["text"])


def sendMessage(token, chatId, message):
    payload = {'text': message}
    r = requests.get("https://api.telegram.org/bot" + token + "/sendMessage?chat_id=" + chatId + "&parse_mode=Markdown", params= payload)
    return r 

def getMessage(token, chatId):
    r = requests.get("https://api.telegram.org/bot" + token + "/getUpdates")
    r = r.text
    r = json.loads(r)
    return r["result"]
    
main ()