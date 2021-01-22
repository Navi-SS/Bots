from Utilities.Youtube import YoutubeService
from Utilities.Happi import HappiServices
from Utilities.Translator import TranslateService
from Utilities.Images import ImageService
import telebot
import pandas as pd
from os import remove

API_TOKEN='API-KEY-Telegram'
bot=telebot.TeleBot(API_TOKEN)

#Services
youtube=YoutubeService()
happi=HappiServices()
trans=TranslateService()
image=ImageService()

#Welcome
@bot.message_handler(commands=['start'])
def send_bienvenida(message):
    datos=pd.read_csv('datos.csv')
    if message.chat.id not in list(datos['id']):
        n=datos.shape[0]
        datos.loc[n]=[message.chat.id,message.chat.first_name]
        datos.to_csv('datos.csv')
    bot.reply_to(message,'Bienvenido a NaviBot usa /help o /example para ver los comandos disponibles')

#Help
@bot.message_handler(commands=["help"])
def send_help(message):
    consult = """/youtube <nombre del video>
/song <nombre de la cancion>
/translate <idioma_origen idioma_destino Frase a traducir>
/help
/example
Envia una imagen con texto y se traducira
Si quieres mas ayuda, contacta al administrador"""
    bot.reply_to(message,consult)

#Example
@bot.message_handler(commands=["example"])
def send_example(message):
    consult = """/youtube life on mars David Bowie
/song walk away Franz Ferdinand
/translate ingles ruso  Hello World
/help
/example
Envia una imagen con texto y se traducira
Si quieres mas ayuda, contacta al administrador"""
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
            bot.reply_to(message,"Error al enviar el nombre del video")
    except IndexError:
        bot.reply_to(message,"No hay nombre del video")

#Return the song information
@bot.message_handler(commands=['song'])
def send_song(message):
    try:
        consult = message.text[6:] # song to look
        song = happi.song(consult)
        if song != None:
            bot.reply_to(message,song,parse_mode="MARKDOWN")
        else:
            bot.reply_to(message,"Error al enviar el nombre de la cancion")
    except IndexError:
        bot.reply_to(message,"No hay nombre de la cancion")

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
            bot.reply_to(message,"Error al enviar la estructura, intenta con uno de los siguientes idiomas: español, ingles, ruso, frances, portugues, aleman, italiano, ucraniano, japones, chino, hindi, arabe, bengali, indonesio")
    except IndexError:
        bot.reply_to(message,"Los idiomas disponibles son: español, ingles, ruso, frances, portugues, aleman, italiano, ucraniano, japones, chino, hindi, arabe, bengali, indonesio")

@bot.message_handler(content_types=['photo'])
def send_photo_translate(message):
    file_id=bot.get_file(message.photo[-1].file_id)
    file_id=file_id.file_path
    download=bot.download_file(file_id)
    with open('image.jpg','wb') as new_file:
        new_file.write(download)
    text=image.read_image('image.jpg')
    if text != None:
        text=trans.all_translate(text)
        bot.reply_to(message,text)
    else:
        bot.reply_to(message,"La imagen no tiene letras")
    remove('image.jpg')



#For other kind of messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "Usa /help o /example para ver todos los comandos del bot")

bot.polling(True)
