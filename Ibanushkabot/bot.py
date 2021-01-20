from Utilities.Youtube import YoutubeService
from Utilities.Happi import HappiServices
from Utilities.Translator import TranslateService
import telebot

API_TOKEN='API-KEY-Telegram'
bot=telebot.TeleBot(API_TOKEN)

#Services
youtube=YoutubeService()
happi=HappiServices()
trans=TranslateService()

#Welcome
@bot.message_handler(commands=['start'])
def send_bienvenida(message):
    bot.reply_to(message,'Welcome to Navibot use /help or /example to see all commands')

#Help
@bot.message_handler(commands=["help"])
def send_help(message):
    consult = """/youtube <video name>
/mylocation
/location <IP>
/song <song name>
/translate <source_language destination_language phrase>
/help
/example
For more help contact the admin"""
    bot.reply_to(message,consult)

#Example
@bot.message_handler(commands=["example"])
def send_example(message):
    consult = """/youtube life on mars David Bowie
/mylocation
/location 172.217.15.14
/song walk away Franz Ferdinand
/translate english spanish Hello World
/help
/example
if you need more help contact the admin"""
    bot.reply_to(message,consult)

#Return the first youtube video
@bot.message_handler(commands=['youtube'])
def send_video(message):
    try:
        consult = message.text[9:] # video to look
        video = youtube.video(consult)
        if video != None:
            bot.reply_to(message,video,parse_mode="MARKDOWN")
        else:
            bot.reply_to(message,"Error sending video name")
    except IndexError:
        bot.reply_to(message,"No video name detected")

#Return your data IP
@bot.message_handler(commands=['mylocation'])
def send_mylocation(message):
    bot.reply_to(message,happi.my_location())

#Return the IP data
@bot.message_handler(commands=['location'])
def send_location(message):
    try:
        consult = message.text[10:] # location to look
        ip_location = happi.location(consult)
        if ip_location != None:
            bot.reply_to(message,ip_location)
        else:
            bot.reply_to(message,"Error sending IP")
    except IndexError:
        bot.reply_to(message,"No IP detected")

#Return the song information
@bot.message_handler(commands=['song'])
def send_song(message):
    try:
        consult = message.text[6:] # song to look
        song = happi.song(consult)
        if song != None:
            bot.reply_to(message,song,parse_mode="MARKDOWN")
        else:
            bot.reply_to(message,"Error sending song name")
    except IndexError:
        bot.reply_to(message,"No song name detected")

#Return the translate phrase
@bot.message_handler(commands=['translate'])
def send_translate(message):
    try:
        consult = message.text[11:] # languages with phrase
        text = trans.translate(consult)
        voice= trans.voice_translate(consult.split()[1],text)
        if text != None and voice != None:
            bot.reply_to(message,text)
            bot.send_voice(message.chat.id,voice)
        else:
            bot.reply_to(message,"Error sending the structure")
    except IndexError:
        bot.reply_to(message,"Error sending the structure")

#For other kind of messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "Use /help or /example to see all bot's commands")

bot.polling(True)
