import requests

# https://api.telegram.org/bot1646568825:AAGV8M7O9WpENt0-AeS8PXBBDoj8MwD8bfg/sendMessage?chat_id=616166895&parse_mode=Markdown&text=hola
def main():
    payload = {'text':"hola soy yassin\nque tal se encuentra USTED!"} 
    r = requests.get("https://api.telegram.org/bot1646568825:AAGV8M7O9WpENt0-AeS8PXBBDoj8MwD8bfg/sendMessage?chat_id=616166895&parse_mode=Markdown", params = payload)
    print (r.url)
main()