# import modules

import requests as req
import time
import datetime
import pytz
import telegram
import globals
from telegram.ext import CommandHandler, Updater
from modules import manage

globals.initialize()

# set update dispatcher
updater = Updater(
    token='2059581474:AAGvXelK7C2pwaOgO5dmFLfAKSruJxR8yqE', use_context=True)

dispatcher = updater.dispatcher

url = 'https://api3.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
bot = telegram.Bot(token='2059581474:AAGvXelK7C2pwaOgO5dmFLfAKSruJxR8yqE')


tz = pytz.timezone('Asia/Tehran')


i = 0
loop = 0
sudo_id = 1324884291
channel_id = -1001728669440

bot.send_message(text='bot was started!', chat_id=sudo_id)

status_handler = CommandHandler('status', manage.status)
sens_handler = CommandHandler('sens', manage.set_sens)

dispatcher.add_handler(status_handler)
dispatcher.add_handler(sens_handler)

updater.start_polling()

while True:
    try:
        r = req.get(url)
        price = float(r.json()['price'])

        if i != 0:

            ekhtelaf = prev_pos - price
            abs_ekhtelaf = abs(ekhtelaf)
            rounded_abs_ekh = round(abs_ekhtelaf)

            if abs_ekhtelaf > globals.alert_sens:

                now = datetime.datetime.now(tz)
                payload = now.strftime('%b %d \n%H:%M (Tehran)')
                changes = int(round(abs_ekhtelaf, -2))
                if ekhtelaf < 0:
                    payload = f'{payload} \n🟢‎ *{changes}$ جهید* \n💎 *{price}$*\n- @riikht'
                else:
                    payload = f'{payload} \n🔴‎ *{changes}$ ریخت* \n💎 *{price}$*\n- @riikht'
                prev_pos = price
                bot.send_message(text=payload, chat_id=sudo_id,
                                 parse_mode=telegram.ParseMode.MARKDOWN)
        else:
            i = 1
            prev_pos = price
    except req.ConnectionError as e:
        bot.send_message(text=str(e), chat_id=sudo_id)

    finally:
        time.sleep(15)
        continue
