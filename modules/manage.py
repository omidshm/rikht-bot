from telegram.ext import CommandHandler, Updater
import psutil
from utils import get_uptime


updater = Updater(
    token='2059581474:AAGvXelK7C2pwaOgO5dmFLfAKSruJxR8yqE', use_context=True)

dispatcher = updater.dispatcher


def status(update, context):
    payload = f'Bot is running\nCPU usage: {psutil.cpu_percent(4)}%\nRam Usage: {psutil.virtual_memory()[2]}%\nUptime: {get_uptime()}'
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=payload)


start_handler = CommandHandler('status', status)
dispatcher.add_handler(start_handler)

updater.start_polling()
