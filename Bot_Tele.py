import telebot, datetime
from telebot import types

api = "2140113357:AAFI14kBSmsShAu82TJI9YBMJHf-CIxbPCY"
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def awal_mengirim(message):
    chatid = message.chat.id
    username = message.from_user.username
    
    bot.send_photo(chatid,open('img/Logo RNS.jpg','rb'))
    bot.send_message(chatid,
    '''
    Selamat datang {} di Portofolio Telegram !!!
    Pembuat Bot ini adalah Robby Nugroho Setiawan (Robby). Ada beberpa penjelasan singkat yang mengenai skill teknologi yang saya miliki :

    /design - Tentang Design Grafis 🎨
    /editing - Tentang editing Vid&Pht 🎬
    /program - Tentang buat program 📱

    Apabila mencari menu yang lain, bisa klik /help untuk membantu anda (-^_^-)
    '''.format(username))

@bot.message_handler(commands=['design'])
def desain(message):
    chatid = message.chat.id
    bot.send_message(chatid,
    '''
    Skill desain grafis berguna untuk komunikasi yang ingin disampaikan secara visual. Menggunakan Tools Pixelab, Canva, Photoshop, dan Corel Draw dalam pembuatan desain grafis. Apabila ingin melihat hasil bisa ketik "Lihat Desain", dan tunggu beberapa menit. 
    ''')

@bot.message_handler(regexp='Lihat Desain')
def tampilanDesain(message):
    chatid = message.chat.id
    bot.send_photo(chatid,open('Gambar Desain/Logo Info Magang.jpg','rb'))
    bot.send_photo(chatid,open('Gambar Desain/MSC Pahlawan.png','rb'))
    bot.send_photo(chatid,open('Gambar Desain/CV Robby 2.png','rb'))

@bot.message_handler(commands=['editing'])
def editing(message):
    chatid = message.chat.id

    bot.send_message(chatid,
    '''
    Skill editing berguna untuk memberikan kesan/pesan menarik seseorang yang melihatnya. Menggunakan Tools video Kinemaster/Filmora/Cupcat, Tools foto Photoshop/Lightroom/CorelDraw. Apabila ingin melihat hasil bisa ketik "Lihat Video" atau "Lihat Foto", dan tunggu beberapa menit. 
    ''')

@bot.message_handler(commands=['program'])
def desain(message):
    chatid = message.chat.id
    markup = types.InlineKeyboardMarkup()
    itemA = types.InlineKeyboardButton('Situs Hasil Ngoding',url='https://github.com/Robbyns99')

    markup.row(itemA)
    bot.send_message(chatid,
    '''
    Skill program/programing berguna untuk pembuatan suatu aplikasi yang membantu aktivitas seseorang. Menggunakan Tools VS Code. Apabila ingin hasil codingan bisa mengunjui website di github. 
    ''',reply_markup=markup)

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