import telebot, datetime
from telebot import types

api = "2140113357:AAFI14kBSmsShAu82TJI9YBMJHf-CIxbPCY"
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
# commands mengarahkan bot pada tulisan/kata yang telah dibuat dengan menambahkan "/" garing
def awal_mengirim(message):
    chatid = message.chat.id
    markup = types.InlineKeyboardMarkup()
    itemA = types.InlineKeyboardButton('Portofolio Web', url='https://robbyns99.github.io/PortofolioWeb/')
    itemB = types.InlineKeyboardButton('Profil', url='https://t.me/Robbyns99/')
    
    bot.send_photo(chatid,open('img/Logo RNS.jpg','rb'))
    bot.send_message(chatid,
    '''
    Selamat datang di Portofolio Telegram !!!
    Pembuat Bot ini adalah Robby Nugroho Setiawan, S.Kom. untuk menambah skill codingan. Kalian bisa menggunakan "/" garis miring untuk membantu kalian.
    Pilih menu yang kalian ingin kunjungi :)
    ''')

    # Assign inline button
    markup.row(itemA,itemB)
    bot.send_message(message.chat.id,'Bisa klik salah satu ^_^',reply_markup=markup)


print('bot start running')

bot.polling()