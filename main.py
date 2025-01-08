import telebot
from telebot import types

# Bot tokeni
BOT_TOKEN = "7632729899:AAG2yXLd_Y-14KmithZ_qe40O6TFnbYT49Q"
bot = telebot.TeleBot(BOT_TOKEN)

# menu Buttonlar
markup = telebot.types.ReplyKeyboardMarkup(True,True)
markup.row("🎓 Kurslar")



# start komandasi
@bot.message_handler(commands=['start'])
def start_comand(message):
    bot.send_message(message.chat.id,"Assalomu alaykum",reply_markup=markup)

# Button boslganada nma qaytarishi
@bot.message_handler(content_types=['text'])
def send(message):
    if message.text=="🎓 Kurslar":
        bot.send_message(message.chat.id,"Assalomu alaykum sizga qaysi tarif kerak")



print("Bot ishga tushdi..")
bot.polling()
