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
sudo_id = 1324884291
channel_id = -1001728669440
while True:
  try:
    r = req.get(url)
    price = float(r.json()['price'])

    if i != 0:

      ekhtelaf = prev_pos - price
      abs_ekhtelaf = abs(ekhtelaf)


      if abs_ekhtelaf > alert_sens:
        now = datetime.datetime.now(tz)
        payload = now.strftime('%b %d \n%H:%M')
        changes = int(round(abs_ekhtelaf,-2))
        if ekhtelaf < 0:
          payload = f'{payload} \n🟢‎ *{changes}$ جهید* \n💎 *{price}$*\n- @riikht'
        else:
          payload = f'{payload} \n🔴‎ *{changes}$ ریخت* \n💎 *{price}$*\n- @riikht'
        prev_pos = price
        bot.send_message(text=payload, chat_id=channel_id,parse_mode=telegram.ParseMode.MARKDOWN)
    else:
      i = 1
      prev_pos = price
  except req.ConnectionError as e:
    bot.send_message(text=str(e), chat_id=sudo_id)

  finally:
    time.sleep(15)
    continue