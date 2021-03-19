import parser_log as p 
cst1 = "00:00:37  ARDR: (14122) MoonShot order replacing DOWN on cur. price: 0.00000323 delay: 1125ms; PriceMin: 2.46% Price: 2.96% hDelta: 21.64% dBTC: 0.93 dBTC5m: 0.96 dMarket: 0.51 dMarket24: -0.28  -- TP: 0.00000323  RD: 1.0  R: YES  D: 125  "
cst2 = "00:07:53  Starting new MoonShot market: BTC-TOMO (strategy <Moontrader d3(30,40) d1(20,30) 1h 300sg>)"
cst3 = "00:09:01  SKY: PumpQ=78 24vol=83 hvol=4 h3vol=9 sellX2=6 PumpsCount=0 SellProb=22% Delta24h=42.30% Delta3h=23.51  d1h: 19%  d15m: 9.1%  PumpD: -0.5%  PumpHDelta: 17.5%  DumpHDelta: 0.9%"

pk = p.packet("","","","","")
pk.clasify(cst1)

print(pk.tipo)
print(pk.num)
print(pk.msg)
print(pk.time)
print(pk.coin)

pk.clasify(cst2)

print(pk.tipo)
print(pk.num)
print(pk.msg)
print(pk.time)
print(pk.coin)

pk.clasify(cst3)

print(pk.tipo)
print(pk.num)
print(pk.msg)
print(pk.time)
print(pk.coin)