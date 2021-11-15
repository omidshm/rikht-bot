import psutil
from modules.utils import get_uptime, validate_sens
import globals

def status(update, context):
    payload = f'Bot is running \nCPU usage: {psutil.cpu_percent(4)}%\nRam Usage: {psutil.virtual_memory()[2]}%\nUptime: {get_uptime()}'
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=payload)

def set_sens(update, context):
    new_sens = validate_sens(context.args[0])
    if new_sens:
        globals.alert_sens = new_sens
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'✅ alert senstivity is set to {new_sens}$ successfully')
    else:
        # raise error
        context.bot.send_message(chat_id=update.effective_chat.id, text="❌ please enter valid number\nlike: /sens 200")