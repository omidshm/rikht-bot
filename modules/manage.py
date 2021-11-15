import psutil
from modules.utils import get_uptime


def status(update, context):
    payload = f'Bot is running\nCPU usage: {psutil.cpu_percent(4)}%\nRam Usage: {psutil.virtual_memory()[2]}%\nUptime: {get_uptime()}'
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=payload)
