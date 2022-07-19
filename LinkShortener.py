import logging
import re
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

API_Key_Url = '25eab58e3f5cc717d5529391d5fd3458e200c'

#Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text('Welcome to Link Shortener, please enter your URL ')

def shorten(update, context):

    url = update.message.text
    if(re.findall('https:', url)):
        name = ''
        r = requests.get('http://cutt.ly/api/api.php?key={}&short={}&name={}'.format(API_Key_Url, url, name))
        json = r.json()
        link = json['url']['shortLink']
        update.message.reply_text("Here's your shortened link " + link)

    else:
        update.message.reply_text('Please enter a valid URL or command')
        update.message.reply_text("Type '/help' to see available commands")

def help(update, context):
        update.message.reply_text("Here's the list of commands: \n  /help -- Help \n /start -- Starts the bot \n")

def error(update, context):
        logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    api_key_telegram = "5538561064:AAGW50CKc5eOH_rGLc-JloADkjF7lM4Ltmc"
    updater = Updater(api_key_telegram, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - recieve links from user
    dp.add_handler(MessageHandler(Filters.text, shorten))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()






