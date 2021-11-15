import psutil
from modules.utils import get_uptime, validate_sens
import globals

def status(update, context):
    payload = f'✅ Bot is running \n🔷 CPU usage: {psutil.cpu_percent(4)}%\n🔷 Ram Usage: {psutil.virtual_memory()[2]}%\n🔷 Uptime: {get_uptime()}'
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=payload)

def set_sens(update, context):
    if context.args != []:
        new_sens = validate_sens(context.args[0])
        if new_sens:
            globals.alert_sens = new_sens
            context.bot.send_message(chat_id=update.effective_chat.id, text=f'✅ alert sensitivity is set to {new_sens}$ successfully')
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="❌ please enter valid number\nlike: /sens 200")
    else:
        # raise error
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'🔷 sens is {globals.alert_sens}$')
