from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def hello(update, context):
  update.message.reply_text("Hello!")

updater = Updater(token="6696162704:AAEil1-RsGu50MXQXNtNRMW6Kdo4cgUI9ZQ")
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, hello))

updater.start_polling()
updater.idle()
