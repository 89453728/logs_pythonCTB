import catch as ck


class packet:
    def __init__(self, tipo, time, coin, num, msg):
        self.tipo = tipo
        self.msg = msg
        self.coin = coin 
        self.time = time 
        self.num = num
    def clasify (self, txt):
        self.time = txt[0:8]
        coin = ""
        for i in range(10,len(txt)) : 
            if (txt[i] != ":" and txt[i] != " "):
                if(i < 17):
                    coin += txt[i] 
                else:
                    self.tipo = 2
                    break
            else:
                self.tipo = 1
                break
        if (self.tipo == 1):        

            # comprobacion si es tipo 1 o 2 ya que se asemejan 
            if(txt[16] != "("):
                self.tipo = 3
            if (self.tipo == 1):
                self.coin = coin 
                self.num = txt[i+3:i+8]
                self.msg = txt[i+10:len(txt)]
            elif(self.tipo == 3):
                self.coin = coin 
                self.num = False
                self.msg = txt[i+2:len(txt)]
        elif (self.tipo == 2):
            self.coin = False
            self.num = False
            self.msg = txt[10:len(txt)]
    def msgClasify (self):
        mesg = self.msg.split(' ')
        response = []
        if (self.tipo == 1):
            if(mesg[0].find("-") > 0):
                mesg[0][mesg[0].find('-')] = "/"
                response[0] = 1 #sub-tipe
                response[1] = mesg[0] #coin
                response[2] = mesg[3] #Buy order
                response[3] = mesg[6] #rate 
                response[4] = mesg[8] #id 
                response[5] = mesg[10] #cid

                return response
            elif(mesg[0] == "MoonShot"):
                response[0] = 2 #sub-tipe
                response[1] = mesg[3] #DOWN o UP
                response[2] = mesg[7] #price
                response[3] = mesg[10] #Ask
                response[4] = mesg[12] #PriceMin %
                response[5] = mesg[14] #Price %
                response[6] = mesg[16] #hDelta %
                response[7] = mesg[18] #dBTC
                response[8] = mesg[20] #dBTC5m
                response[9] = mesg[22] #dMarket
                response[10] = mesg[24] #dMarket24
                return response
            elif(mesg[0] == "Order"):
                response[0] = 3 #sub-tipe
                response[1] = mesg[1] #num-order
                return response 
            elif[mesg[0] == "BUY"]:
                response[0] = 4 #sub-tipe
                return response 
            else: 
                response[0] = -1
                return response 
        elif (self.tipo == 2):
            pass
        else:
            pass
        
