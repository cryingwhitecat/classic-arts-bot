import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater
from telegram.ext import MessageHandler,Filters
from telegram.ext import CommandHandler
import logging
from config import *

class Handler:

    handlers={}
    infos=dict()

    def AddHandler(key,value):
        Handler.handlers[key]=value

    def AddInfo(key,value):
        Handler.infos[key]=value

    def start(bot,update):
        markup=telegram.ReplyKeyboardMarkup(Config.mainMarkup)
        bot.send_message(chat_id=update.message.chat_id,text="Hello World",reply_markup=markup)

    def handleInfo(bot,update):
        name=update.message.text.split(" ")[1].lower()
        try:
            info=Handler.infos[name]
        except KeyError as e:
            bot.send_message(chat_id=update.message.chat_id,text="No artist with this name in our database.")
        bot.send_message(chat_id=update.message.chat_id,text=info)

    #returns the keyboard with all paintings painted by Magritte
    def handleMargitte(bot,update):
        #image=open('Data/Paintings/Magritte-The Empire of The Light.jpg','rb')
        markup=telegram.ReplyKeyboardMarkup(Config.magritteMarkup)
        bot.send_message(chat_id=update.message.chat_id,text="Choose The Painting: ",reply_markup=markup)

    #returns the "Golconde" Painting
    def handleGolconde(bot,update):
        bot.send_message(chat_id=update.message.chat_id,text="Golconde,1953")
        bot.send_photo(chat_id=update.message.chat_id,photo=Config.golcondeUrl,
        reply_markup=telegram.ReplyKeyboardMarkup(Config.returnMarkup))

    #returns the "Guernica" panno
    def handleGuernica(bot,update):
        chat_id=update.message.chat_id
        bot.send_message(chat_id=chat_id,text="Guernica,1938")
        bot.send_photo(chat_id=chat_id,photo=Config.guernicaUrl,
        reply_markup=telegram.ReplyKeyboardMarkup(Config.returnMarkup))

    #returns to the artists page
    def handleReturnToArtists(bot,update):
        markup=telegram.ReplyKeyboardMarkup(Config.artistsMarkup)
        bot.send_message(chat_id=update.message.chat_id,text="Returning To The Artists...",reply_markup=markup)

    #returns the keyboard with the main menu
    def handleReturnToMain(bot,update):
        markup=telegram.ReplyKeyboardMarkup(Config.mainMarkup)
        bot.send_message(chat_id=update.message.chat_id,text="Returning To The Main...",reply_markup=markup)
    
    def handleAvignon(bot,update):
        chat_id=update.message.chat_id
        bot.send_message(chat_id=chat_id,text="Les Demoiselles d'Avignon,1907")
        bot.send_photo(chat_id=chat_id,photo=Config.avignonUrl,
        reply_markup=telegram.ReplyKeyboardMarkup(Config.returnMarkup))

    #returns the "The Empire Of The Light" painting 
    def handleEmpire(bot,update):
        bot.send_message(chat_id=update.message.chat_id,text="The Empire Of The Light,1953(Unfinished)")
        bot.send_photo(chat_id=update.message.chat_id,photo=Config.empireUrl)

    def handlePicasso(bot,update):
        #image=open('Data/Paintings/Picasso-Guernica.jpg','rb')
        markup=telegram.ReplyKeyboardMarkup(Config.picassoMarkup)
        bot.send_message(chat_id=update.message.chat_id,text="Choose The Painting: ",reply_markup=markup)

   
    def handlePaintings(bot,update):
        replyMarkup=telegram.ReplyKeyboardMarkup(Config.artistsMarkup)
        bot.send_message(chat_id=update.message.chat_id,text="Choose the Artist: ",reply_markup=replyMarkup)   

    def handleMessage(bot,update):
        Handler.handlers[update.message.text](bot=bot,update=update)
        # if update.message.text == 'Paintings':
        #     Handler.handlePaintings(bot=bot,update=update)
        # if update.message.text== 'Picasso':
        #     Handler.handlePicasso(bot=bot,update=update)
        # if update.message.text == 'Magritte':
        #     Handler.handleMargitte(bot=bot,update=update)
        # if update.message.text == 'Golconde':
        #     Handler.handleGolconde(bot=bot,update=update)
        # if update.message.text == 'The Empire Of The Light':
        #     Handler.handleEmpire(bot=bot,update=update)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

updater=Updater(token=Config.token)
dispatcher=updater.dispatcher

Handler.AddInfo('magritte',Config.magritteInfo)
Handler.AddInfo('picasso',Config.picassoInfo)

Handler.AddHandler('Magritte',Handler.handleMargitte)
Handler.AddHandler('Picasso',Handler.handlePicasso)
Handler.AddHandler('Golconde',Handler.handleGolconde)
Handler.AddHandler('The Empire Of The Light',Handler.handleEmpire)
Handler.AddHandler('Paintings',Handler.handlePaintings)
Handler.AddHandler('Return To The Main Menu',Handler.handleReturnToMain)
Handler.AddHandler('Return To Artists',Handler.handleReturnToArtists)
Handler.AddHandler('Guernica',Handler.handleGuernica)
Handler.AddHandler("Les Demoiselles d'Avignon",Handler.handleAvignon)
infoHandler=CommandHandler('infoAbout',Handler.handleInfo)

ch=CommandHandler('start',Handler.start)
mh=MessageHandler(Filters.text,Handler.handleMessage)
dispatcher.add_handler(ch)
dispatcher.add_handler(mh)
dispatcher.add_handler(infoHandler)
updater.start_polling()
