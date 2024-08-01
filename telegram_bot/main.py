import telebot

Token = "7091716608:AAE5Ti34dZxT9sBLtPMTKLIDNYgaAkugIOw"

bot = telebot.TeleBot(Token)

@bot.message_handler(["start"])
def start(message):
    bot.reply_to(message, "Welcome To Mr Kartik Calculator")

@bot.message_handler(["help"])

def help(message):
    bot.reply_to(message, "How Can Help You")
bot.polling()