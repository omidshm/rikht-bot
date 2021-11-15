from telegram.ext import Updater
from telegram.ext import CommandHandler
from modules.utils import validate_sens

updater = Updater(token='2059581474:AAGvXelK7C2pwaOgO5dmFLfAKSruJxR8yqE', use_context=True)

dispatcher = updater.dispatcher


def set_sens(update, context):
    if context.args != []:
        new_sens = validate_sens(context.args[0])
        if new_sens:
            globals.alert_sens = new_sens
            context.bot.send_message(chat_id=update.effective_chat.id, text=f'✅ alert senstivity is set to {new_sens}$ successfully')
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="❌ please enter valid number\nlike: /sens 200")
    else:
        # raise error
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'❇️ sens is {globals.alert_sens}$')


caps_handler = CommandHandler('sens', set_sens)
dispatcher.add_handler(caps_handler)

updater.start_polling()
