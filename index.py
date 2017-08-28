import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler,Filters
from telegram.ext import CommandHandler
import logging
import configparser
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
config = configparser.ConfigParser()
config.readfp(open(r'config.cfg'))
token=config.get('Section1','token')
updater=Updater(token='448011630:AAGTjU7CGUsGNx1reZJJN79_n3r-aDHXM8o')
dispatcher=updater.dispatcher

def start(bot,update):
    markup=[['Paintings']]
    markup=telegram.ReplyKeyboardMarkup(markup)
    bot.send_message(chat_id=update.message.chat_id,text="Hello World",reply_markup=markup)

def handlePicasso(bot,update):
    image=open('Data/Paintings/Picasso-Guernica.jpg','rb')
    bot.send_message(chat_id=update.message.chat_id,text="Picasso-Guernica,1938")
    bot.send_photo(chat_id=update.message.chat_id,photo=image)

def handleMargitte(bot,update):
    image=open('Data/Paintings/Magritte-The Empire of The Light.jpg','rb')
    bot.send_message(chat_id=update.message.chat_id,text="Magritte-The Emprire of The Light,1953(Unfinished)")
    bot.send_photo(chat_id=update.message.chat_id,photo=image)

def handlePaintings(bot,update):
    markup=[['Picasso','Magritte']]
    replyMarkup=telegram.ReplyKeyboardMarkup(markup)
    bot.send_message(chat_id=update.message.chat_id,text="Choose the Artist: ",reply_markup=replyMarkup)   
def handleMessage(bot,update):
    if update.message.text == 'Paintings':
        handlePaintings(bot=bot,update=update)
    if(update.message.text== 'Picasso'):
        handlePicasso(bot=bot,update=update)
    if(update.message.text == 'Magritte'):
        handleMargitte(bot=bot,update=update)

ch=CommandHandler('start',start)
mh=MessageHandler(Filters.text,handleMessage)
dispatcher.add_handler(ch)
dispatcher.add_handler(mh)

updater.start_polling()