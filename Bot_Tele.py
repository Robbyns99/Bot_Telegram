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
    itemB = types.InlineKeyboardButton('My Profil', url='http://t.me/6289609785921')
    
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

@bot.message_handler(commands=['help'])
def bantuan(message):
    chatid = message.chat.id

    bot.send_message(chatid,
    '''
    Kalian bisa pilih menu beriku :
    /start - Untuk menampilkan tampilan awal portofolio tele bot 💻
    /help - Membantu anda memilih menu yang ada di bot ⁉️
    /contact - Bisa di hubungi memalui kontak yang ada 📥
    /portofolioweb - Mengarahkan ke website portofolio 🌐
    ''')

@bot.message_handler(commands=['contact'])
def kontak(message):
    markup = types.InlineKeyboardMarkup()
    itemA = types.InlineKeyboardButton('📞 Bisa chat WA', url='http://wa.me/6289609785921')
    itemB = types.InlineKeyboardButton('📷 Bisa chat IG', url='https://www.instagram.com/robbyns99/')
    itemC = types.InlineKeyboardButton('📧 Bisa chat Email', url='mailto:Robbynugrohos02@gmail.com')
    itemD = types.InlineKeyboardButton('💬 Bisa chat Tele', url='http://t.me/6289609785921')

    markup.row(itemA,itemB)
    markup.row(itemC,itemD)
    bot.send_message(message.chat.id,'Bisa dihubungi Sosmed berikut: ',reply_markup=markup)

@bot.message_handler(commands=['portofolioweb'])
def portofolio_web(message):
   markup = types.InlineKeyboardMarkup()
   itemA = types.InlineKeyboardButton('Portofolio Web', url='https://robbyns99.github.io/PortofolioWeb/')

   markup.row(itemA)
   bot.send_message(message.chat.id,'Klik menuju web Portofolio',reply_markup=markup)

print('bot start running')

bot.polling()