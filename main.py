import os
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler

from flask import Flask
app = Flask(__name__)

my_secret = os.environ['TOKEN']

@app.route('/')
def home():
  return "Your bot is alive!"


def help_command(update: Update, context: CallbackContext):
  htext = "Hey bro, it's me, your bot brother"
  chat_id = update.message.chat_id
  context.bot.send_chat_action(chat_id=chat_id, action=telegram.chataction.ChatAction.TYPING)
  update.message.reply_text(htext)

def keyboards(update: Update, context: CallbackContext):
  bot = context.bot
  chat_id = update.message.chat_id
  location_keyboard = telegram.KeyboardButton(text="send_location", request_location=True)

  contact_keyboard = telegram.KeyboardButton(text="send_contact", request_contact=True)

  custom_keyboard = [[ location_keyboard, contact_keyboard ]]

  reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)

  bot.send_message(chat_id=chat_id, 
                  text="Would you mind sharing your location and contact with me?",
                  reply_markup=reply_markup)


def message_handler(update: Update, context: CallbackContext):
  update.message.reply_text("Heeey throoo")


def main():
  updater = Updater(os.getenv("TOKEN"))

  dispatcher = updater.dispatcher

  dispatcher.add_handler(CommandHandler('start', help_command))
  dispatcher.add_handler(CommandHandler('keyboards', keyboards))
  # dispatcher.add_handler(MessageHandler(, message_handler))

  updater.start_polling()

  app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
  main()
