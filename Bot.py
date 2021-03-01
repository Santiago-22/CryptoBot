import discord 
import os
import pytz
from pycoingecko import CoinGeckoAPI
from datetime import datetime
from pytz import timezone
from conectado import conectado


client = discord.Client()

def valor_btc(moeda: str = 'BRL', moeda2 = "USD"):
    cg = CoinGeckoAPI()

    IST = pytz.timezone('Brazil/East') 
    agora = datetime.now(IST)

    data = agora.strftime("%d/%m/%y")
    hora = agora.strftime("%H:%M")
    data_fo = ":calendar_spiral: Em {} às {}".format(data,hora)

    result = cg.get_price(ids='bitcoin', vs_currencies='{}'.format(moeda),include_24hr_change ='true')

    moeda_valor = result['bitcoin'][moeda.lower()]
    moeda_24_hrs = result['bitcoin']['{}_24h_change'.format(moeda.lower())]

    moeda_fo = float("%.2f" %moeda_24_hrs)
    if moeda_fo > 0:
      frase3 = ":chart_with_upwards_trend: 24h: {}%".format(moeda_fo)
    elif moeda_fo < 0:
      frase3 = ":chart_with_downwards_trend: 24h: {}%".format(moeda_fo)


    formatado = list(str(moeda_valor))
    formatado.insert(3,'.')
    moeda_valor = "".join(formatado)
    frase = ":flag_br: R$ {},00".format(moeda_valor)

    ######
    result = cg.get_price(ids='bitcoin', vs_currencies='{}'.format(moeda2))

    moeda_valor2 = result['bitcoin'][moeda2.lower()]
    formatado2 = list(str(moeda_valor2))
    formatado2.insert(2,'.')
    moeda_valor2 = "".join(formatado2)
    frase2 = ":flag_us: $ {},00".format(moeda_valor2)

  
    return "Valor atual da Bitcoin :money_with_wings:"+'\n'+'\n'+frase+'\n'+frase2+'\n'+'\n'+frase3+'\n'+'\n'+data_fo

###########################
def valor_eth(moeda: str = 'BRL', moeda2 = "USD"):
    cg = CoinGeckoAPI()

    IST = pytz.timezone('Brazil/East') 
    agora = datetime.now(IST)

    data = agora.strftime("%d/%m/%y")
    hora = agora.strftime("%H:%M")
    data_fo = ":calendar_spiral: Em {} às {}".format(data,hora)

    result = cg.get_price(ids='ethereum', vs_currencies='{}'.format(moeda),include_24hr_change ='true')

    moeda_valor = result['ethereum'][moeda.lower()]
    moeda_24_hrs = result['ethereum']['{}_24h_change'.format(moeda.lower())]

    moeda_fo = float("%.2f" %moeda_24_hrs)
    if moeda_fo > 0:
      frase3 = ":chart_with_upwards_trend: 24h: {}%".format(moeda_fo)
    elif moeda_fo < 0:
      frase3 = ":chart_with_downwards_trend: 24h: {}%".format(moeda_fo)


    formatado = list(str(moeda_valor))
    formatado.insert(1,'.')
    moeda_valor = "".join(formatado)
    troca_ponto = moeda_valor.rfind(".")
    moeda_valor = moeda_valor[:troca_ponto] + "," + moeda_valor[troca_ponto+1:]
    frase = ":flag_br: R$ {}".format(moeda_valor)

    ######
    result = cg.get_price(ids='ethereum', vs_currencies='{}'.format(moeda2))

    moeda_valor2 = result['ethereum'][moeda2.lower()]
    formatado2 = list(str(moeda_valor2))
    formatado2.insert(1,'.')
    moeda_valor2 = "".join(formatado2)
    troca_ponto = moeda_valor2.rfind(".")
    moeda_valor2 = moeda_valor2[:troca_ponto] + "," + moeda_valor2[troca_ponto+1:]
    frase2 = ":flag_us: $ {}".format(moeda_valor2)

  
    return "Valor atual do Ethereum:money_with_wings:"+'\n'+'\n'+frase+'\n'+frase2+'\n'+'\n'+frase3+'\n'+'\n'+data_fo

#######################

def valor_xrp(moeda: str = 'BRL', moeda2 = "USD"):
    cg = CoinGeckoAPI()

    IST = pytz.timezone('Brazil/East') 
    agora = datetime.now(IST)

    data = agora.strftime("%d/%m/%y")
    hora = agora.strftime("%H:%M")
    data_fo = ":calendar_spiral: Em {} às {}".format(data,hora)

    result = cg.get_price(ids='ripple', vs_currencies='{}'.format(moeda),include_24hr_change ='true')

    moeda_valor = result['ripple'][moeda.lower()]
    moeda_24_hrs = result['ripple']['{}_24h_change'.format(moeda.lower())]

    moeda_fo = float("%.2f" %moeda_24_hrs)
    if moeda_fo > 0:
      frase3 = ":chart_with_upwards_trend: 24h: {}%".format(moeda_fo)
    elif moeda_fo < 0:
      frase3 = ":chart_with_downwards_trend: 24h: {}%".format(moeda_fo)


    formatado = list(str(moeda_valor))
    moeda_valor = "".join(formatado)
    troca_ponto = moeda_valor.rfind(".")
    moeda_valor = moeda_valor[:troca_ponto] + "," + moeda_valor[troca_ponto+1:]
    frase = ":flag_br: R$ {}".format(moeda_valor)

    ######
    result = cg.get_price(ids='ripple', vs_currencies='{}'.format(moeda2))

    moeda_valor2 = result['ripple'][moeda2.lower()]
    moeda_valor2 = float(moeda_valor2)
    moeda_valor2 = ("%.2f" %moeda_valor2)
    formatado2 = list(str(moeda_valor2))
    moeda_valor2 = "".join(formatado2)
    troca_ponto = moeda_valor2.rfind(".")
    moeda_valor2 = moeda_valor2[:troca_ponto] + "," + moeda_valor2[troca_ponto+1:]
    frase2 = ":flag_us: $ {}".format(moeda_valor2)

  
    return "Valor atual do Ripple :money_with_wings:"+'\n'+'\n'+frase+'\n'+frase2+'\n'+'\n'+frase3+'\n'+'\n'+data_fo
############################

def valor_ltc(moeda: str = 'BRL', moeda2 = "USD"):
    cg = CoinGeckoAPI()

    IST = pytz.timezone('Brazil/East') 
    agora = datetime.now(IST)

    data = agora.strftime("%d/%m/%y")
    hora = agora.strftime("%H:%M")
    data_fo = ":calendar_spiral: Em {} às {}".format(data,hora)

    result = cg.get_price(ids='litecoin', vs_currencies='{}'.format(moeda),include_24hr_change ='true')

    moeda_valor = result['litecoin'][moeda.lower()]
    moeda_24_hrs = result['litecoin']['{}_24h_change'.format(moeda.lower())]

    moeda_fo = float("%.2f" %moeda_24_hrs)
    if moeda_fo > 0:
      frase3 = ":chart_with_upwards_trend: 24h: {}%".format(moeda_fo)
    elif moeda_fo < 0:
      frase3 = ":chart_with_downwards_trend: 24h: {}%".format(moeda_fo)


    formatado = list(str(moeda_valor))
    formatado.insert(1,'.')
    moeda_valor = "".join(formatado)
    troca_ponto = moeda_valor.rfind(".")
    moeda_valor = moeda_valor[:troca_ponto] + "," + moeda_valor[troca_ponto+1:]
    frase = ":flag_br: R$ {}".format(moeda_valor)

    ######
    result = cg.get_price(ids='litecoin', vs_currencies='{}'.format(moeda2))

    moeda_valor2 = result['litecoin'][moeda2.lower()]
    formatado2 = list(str(moeda_valor2))
    moeda_valor2 = "".join(formatado2)
    troca_ponto = moeda_valor2.rfind(".")
    moeda_valor2 = moeda_valor2[:troca_ponto] + "," + moeda_valor2[troca_ponto+1:]
    frase2 = ":flag_us: $ {}".format(moeda_valor2)

  
    return "Valor atual da Litecoin:money_with_wings:"+'\n'+'\n'+frase+'\n'+frase2+'\n'+'\n'+frase3+'\n'+'\n'+data_fo
    ############################

def valor_stl(moeda: str = 'BRL', moeda2 = "USD"):
    cg = CoinGeckoAPI()

    IST = pytz.timezone('Brazil/East') 
    agora = datetime.now(IST)

    data = agora.strftime("%d/%m/%y")
    hora = agora.strftime("%H:%M")
    data_fo = ":calendar_spiral: Em {} às {}".format(data,hora)

    result = cg.get_price(ids='stellar', vs_currencies='{}'.format(moeda),include_24hr_change ='true')

    moeda_valor = result['stellar'][moeda.lower()]
    moeda_24_hrs = result['stellar']['{}_24h_change'.format(moeda.lower())]

    moeda_fo = float("%.2f" %moeda_24_hrs)
    if moeda_fo > 0:
      frase3 = ":chart_with_upwards_trend: 24h: {}%".format(moeda_fo)
    elif moeda_fo < 0:
      frase3 = ":chart_with_downwards_trend: 24h: {}%".format(moeda_fo)


    formatado = list(str(moeda_valor))
    moeda_valor = "".join(formatado)
    troca_ponto = moeda_valor.rfind(".")
    moeda_valor = moeda_valor[:troca_ponto] + "," + moeda_valor[troca_ponto+1:]
    frase = ":flag_br: R$ {}".format(moeda_valor)

    ######
    result = cg.get_price(ids='stellar', vs_currencies='{}'.format(moeda2))

    moeda_valor2 = result['stellar'][moeda2.lower()]
    moeda_valor2 = float(moeda_valor2)
    moeda_valor2 = ("%.2f" %moeda_valor2)
    formatado2 = list(str(moeda_valor2))
    moeda_valor2 = "".join(formatado2)
    troca_ponto = moeda_valor2.rfind(".")
    moeda_valor2 = moeda_valor2[:troca_ponto] + "," + moeda_valor2[troca_ponto+1:]
    frase2 = ":flag_us: $ {}".format(moeda_valor2)

  
    return "Valor atual do Stellar :money_with_wings:"+'\n'+'\n'+frase+'\n'+frase2+'\n'+'\n'+frase3+'\n'+'\n'+data_fo

############################
def valor_cdn(moeda: str = 'BRL', moeda2 = "USD"):
    cg = CoinGeckoAPI()

    IST = pytz.timezone('Brazil/East') 
    agora = datetime.now(IST)

    data = agora.strftime("%d/%m/%y")
    hora = agora.strftime("%H:%M")
    data_fo = ":calendar_spiral: Em {} às {}".format(data,hora)

    result = cg.get_price(ids='cardano', vs_currencies='{}'.format(moeda),include_24hr_change ='true')

    moeda_valor = result['cardano'][moeda.lower()]
    moeda_24_hrs = result['cardano']['{}_24h_change'.format(moeda.lower())]

    moeda_fo = float("%.2f" %moeda_24_hrs)
    if moeda_fo > 0:
      frase3 = ":chart_with_upwards_trend: 24h: {}%".format(moeda_fo)
    elif moeda_fo < 0:
      frase3 = ":chart_with_downwards_trend: 24h: {}%".format(moeda_fo)


    formatado = list(str(moeda_valor))
    moeda_valor = "".join(formatado)
    troca_ponto = moeda_valor.rfind(".")
    moeda_valor = moeda_valor[:troca_ponto] + "," + moeda_valor[troca_ponto+1:]
    frase = ":flag_br: R$ {}".format(moeda_valor)

    ######
    result = cg.get_price(ids='cardano', vs_currencies='{}'.format(moeda2))

    moeda_valor2 = result['cardano'][moeda2.lower()]
    moeda_valor2 = float(moeda_valor2)
    moeda_valor2 = ("%.2f" %moeda_valor2)
    formatado2 = list(str(moeda_valor2))
    moeda_valor2 = "".join(formatado2)
    troca_ponto = moeda_valor2.rfind(".")
    moeda_valor2 = moeda_valor2[:troca_ponto] + "," + moeda_valor2[troca_ponto+1:]
    frase2 = ":flag_us: $ {}".format(moeda_valor2)

  
    return "Valor atual do Cardano :money_with_wings:"+'\n'+'\n'+frase+'\n'+frase2+'\n'+'\n'+frase3+'\n'+'\n'+data_fo
  
##########################

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$bitcoin'or '$Bitcoin'):
    bitcoin = valor_btc()
    await message.channel.send(bitcoin)
  
  elif message.content.startswith('$ethereum' or '$Ethereum'):
    ethereum = valor_eth()
    await message.channel.send(ethereum)
  
  elif message.content.startswith('$ripple'):
    ripple = valor_xrp()
    await message.channel.send(ripple)
  
  elif message.content.startswith('$litecoin'):
    litecoin = valor_ltc()
    await message.channel.send(litecoin)
  
  elif message.content.startswith("$stellar"):
    stellar = valor_stl()
    await message.channel.send(stellar)
  
  elif message.content.startswith("$cardano"):
    cardano = valor_cdn()
    await message.channel.send(cardano)
  
  elif message.content.startswith("$list"):
    await message.channel.send("As criptomoedas suportadas até o momento são:"+'\n'+"Bitcoin (BTC)"+'\n'+"Cardano (ADA)"+'\n'+"Ethereum (ETH)"+'\n'+"Litecoin (LTC)"+'\n'+"Ripple (XRP)"+'\n'+"Stellar (XLM)"+'\n'":coin: Mais moedas em breve! :coin:")
  
  elif message.content.startswith('$What do you do?'):
    await message.channel.send('I can tell the price of cryptocurrency in real time!')

conectado()
client.run(os.getenv('TOKEN'))

