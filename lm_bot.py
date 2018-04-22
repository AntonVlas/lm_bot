# Настройки
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.user import User
from telegram import user
import apiai, json, requests
updater = Updater(token='573439927:AAEbWeftLfveTAvIts84mmR33-PCXf7aNv4') # Токен API к Telegram
dispatcher = updater.dispatcher
# Обработка команд
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')
def textMessage(bot, update):
    request = apiai.ApiAI('46067d53fad14c77bc843e2bca26d8fc').text_request() # Токен API к Dialogflow
    request.lang = 'ru' # На каком языке будет послан запрос
    request.session_id = 'BatlabAIBot' # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.query = update.message.text # Посылаем запрос к ИИ с сообщением от юзера
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech'] # Разбираем JSON и вытаскиваем ответ
    # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=n + ' ' +n2 +', ' + response)
    else:
        n=str(update.message.from_user.first_name)
        n2=str(update.message.from_user.last_name)
        тт=update.message.chat_id
        bot.send_message(chat_id=update.message.chat_id, text=n + ' ' +n2 +', Я Вас не совсем понял!')
       #bot.send_message(chat_id='@vlaslm_bot', text=n + ', Я Вас не совсем понял!')
# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()


