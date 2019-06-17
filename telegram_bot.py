import telegram

bot = telegram.Bot(token='762039497:AAEtmEPdLhBoP2ooI-r0eY-uAPht5UZjb8Q')

#for i in bot.getUpdates():
    #print(i.message)

bot.send_message(chat_id= 858972016, text='테스트테스트')