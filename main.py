# import modules

import json
import requests as req
import time
import datetime
import pytz
import telegram

url = 'https://api3.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
bot = telegram.Bot(token='2059581474:AAGvXelK7C2pwaOgO5dmFLfAKSruJxR8yqE')


tz = pytz.timezone('Asia/Tehran')

i = 0
alert_sens = 200
chat_id = 1324884291
while True:
  r = req.get(url)
  price = float(r.json()['price'])

  if i != 0:

    ekhtelaf = prev_pos - price
    abs_ekhtelaf = abs(ekhtelaf)


    if abs_ekhtelaf > alert_sens:
      now = datetime.datetime.now(tz)
      payload = now.strftime('%b %d \n%H:%M (Tehran)')
      if ekhtelaf < 0:
        payload = f'{payload} \n🟢 Pumped Over 200$ \n💎 ${price}\n- @riikht'
      else:
        payload = f'{payload} \n🔴 Crashed Over 200$ \n💎 ${price}\n- @riikht'
      bot.send_message(text=payload, chat_id=chat_id)
      prev_pos = price
  else:
    i = 1
    prev_pos = price

  time.sleep(5)