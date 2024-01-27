import json
import telebot,os
import glob, os
from telebot import types
from random import randint
import random,re
from time import sleep

bot = telebot.TeleBot("6541321830:AAHYudb3OJHTnlOl5oGQII2rH9ftbDqu5kk")
ch = types.InlineKeyboardButton(text="ZZBank.",callback_data = "RebackBank")
ch2 = types.InlineKeyboardButton(text="TomeBank.",callback_data = "SpaceBank")
ch3 = types.InlineKeyboardButton(text="- Delete Account.",callback_data = "d")


@bot.message_handler(commands=['start'])
def start(message):
    aw = glob.glob('./*.txt')
    if f"c{message.chat.id}.txt" not in aw:
        with open(f"c{message.chat.id}.txt","a")as xs:
            bot.reply_to(message,text=f"""<strong>
👋 مرحبا {message.chat.first_name},
- مرحبا بكم في bank tokyo .
- يمكنك إنشاء حساب مصرفي خاص بك واللعب لتكون وحشًا في القائمة الأولى! .
- يمكنك الحصول على جوائز في الروبوت والمزيد!
- أضف بوت إلى مجموعتك أو يمكنك استخدامه هنا! .

 ━━━━━━━━━━━━━━━━━
أرسل /bank لإنشاء حساب! .

</strong>""",parse_mode="html")
            xs.write("50")
            xs.close()
    else:
        afb = f"""
👋 مرحبا {message.chat.first_name},
- مرحبا بكم في bank tokyo .
- يمكنك إنشاء حساب مصرفي خاص بك واللعب لتكون وحشًا في القائمة الأولى! .
- يمكنك الحصول على جوائز في الروبوت والمزيد!
- أضف بوت إلى مجموعتك أو يمكنك استخدامه هنا! .

 ━━━━━━━━━━━━━━━━━
أرسل /bank لإنشاء حساب! .
        """
        
@bot.message_handler(commands=["balance"])
def a(message):
    f = open(f"{message.chat.id}.txt").read()
    fl = open(f"c{message.chat.id}.txt").read()
    nn = f.split(":")[1]
    balance = f.split(":")[3]
    apcc = fl
    bot.reply_to(message,f"<strong>رصيدك الان : {apcc} 💵</strong>",parse_mode="html")
@bot.message_handler(commands=["my"])
def a(message):
    global acc
    idp = message.from_user.id
    print(idp)
    aw = glob.glob('./*.txt')
    print(aw)
    if f"./{message.chat.id}.txt" in aw:
      me = types.InlineKeyboardMarkup()
      me.row_width = 1
      me.add(ch3)
      with open(f"{message.chat.id}.txt","r+")as df:
          
          f = open(f"{message.chat.id}.txt").read()
          fpp = open(f"blockTip.txt","r+")
          fpp.truncate(0)
          fppp = open(f"block.txt","r+")
          fppp.truncate(0)
          fl = open(f"c{message.chat.id}.txt").read()
          nn = f.split(":")[1]
          balance = f.split(":")[3]
          acc = fl
          ifn = f"""
- اسمك : {nn} .
- ايدي حسابك البنكي : {balance} .
- فلوسك : {acc} 💵.
- ================= -
          """
          bot.reply_to(message,f"<strong>{ifn}</strong>",parse_mode="html",reply_markup=me)
         
          df.close()
    else:
          bot.reply_to(message,f"<strong>عذرا انته لا تمتلك حساب بنكي\nيرجع ارسال الامر /bank لانشاء حساب.</strong>",parse_mode="html")
          mounth(message)
@bot.message_handler(commands=["bank"])
def mounth(message):
    global msg1
    iddd = message.from_user.id
    aw = glob.glob('./*.txt')
    print(aw)
    print(message.chat.first_name)
    if f"./{message.chat.id}.txt" in aw:
        bot.reply_to(message,f"<strong>عذرا عزيزي انته تمتلك حساب فعلا !</strong>",parse_mode="html")
        
    else:
        me = types.InlineKeyboardMarkup()
        me.row_width = 1
        me.add(ch,ch2)
        msg1 = message.text
        sent = bot.reply_to(message, text="<strong>ارسل اسم حسابك البنكي</strong>",parse_mode="html",reply_markup=me)

@bot.message_handler(func=lambda m:"راتب")
def ga(message):
    global acc
    ms = message.text
    print(message)
    if ms == "delete" or ms == "حذف":
        os.system(f"rm -rf {message.from_user.id}.txt")
        bot.reply_to(message,f"<strong>Done Delete your Account .</strong>",parse_mode="html")
    if ms == "help" or ms == "الاوامر" or ms == "امر":
        help = """
اهلا بك في لستة الاوامر
1- استثمار (مبلغ) 
مثال : استثمار 10000
2- حظ (مبلغ)
مثال : حظ 1000
3- مضاربه (مبلغ)
مثال : مضاربه 1000
4- راتب
5- كنز
6-بخشيش
7- فلوسي | لرؤية فلوسك

تم جلب كامل اللسته 
        """
        bot.reply_to(message,f"<strong>{help}</strong>",parse_mode="html")
    if ms == "فلوسي" or ms == "فلوس":
        fl = open(f"c{message.from_user.id}.txt").read()
        bot.reply_to(message,f"<strong>فلوسك الحاليا : <code>{fl}</code> 💵</strong>",parse_mode="html")
        
    if ms == "كنز":
          ca = open(f"blockTip.txt").read()
          if f"{message.chat.username}" in ca:
              bot.reply_to(message,f"<strong>So Quick!\nCome Here Again After 10m!</strong>",parse_mode="html")
          else:
              
              rt = randint(50,1000000)
              ratb = rt
              acc = open(f"c{message.chat.id}.txt").read()
              ga = float(ratb) + float(acc)
              print(ratb)
              print(ga)
              with open(f"c{message.chat.id}.txt","r+")as fs:
                  fs.truncate(0)
              with open(f"c{message.chat.id}.txt","w")as va:
                  va.write(f"{ga}")
              bot.reply_to(message,f"<strong>💸 مبروك كنزك متاح!🤩\n- النقاط المكسبه {ratb} 💵.\n- نقاطك الحالية : {ga} 💵 .</strong>",parse_mode="html")
              with open(f"blockTip.txt","w")as df:
                 df.write(f"{message.chat.username}\n")
                 
                 df.close()
    if "استثمار" in ms:
        value = message.text.replace("استثمار","")
        ls = ["Done","Fail"]
        
        if "Done" in ls:
            ppe = open(f"c{message.from_user.id}.txt").read()
            kf = float(value) + float(randint(float(ppe),float(ppe)))
            with open(f"c{message.from_user.id}.txt","r+")as fs:
                  fs.truncate(0)
            with open(f"c{message.from_user.id}.txt","w")as va:
                  va.write(f"{kf}")
            d = ["1%","2%","4%","8%","9%"]
            raa = random.choice(d)
            bot.reply_to(message,f"""<strong>
- استثمار ناجح  ✅
- نسبة الربح  ↢ {raa}
- مبلغ الربح  ↢ ( {ppe} 💵 )
- نقاطك الحاليا  ↢ ( {kf}  💵 )
.</strong>""",parse_mode="html")
    if f"حظ {ms}"in message.text:
        value = message.text.replace("حظ","")
        ls = ["Done","Fail"]
        sv = random.choice(ls)
        if "Done" in sv:
            pe = open(f"c{message.chat.id}.txt").read()
            kf = int(value) + int(randint(int(pe),int(pe)))
            with open(f"c{message.chat.id}.txt","r+")as fs:
                  fs.truncate(0)
            with open(f"c{message.chat.id}.txt","w")as va:
                  va.write(f"{kf}")
            bot.reply_to(message,f"""<strong>
- مبروك حض ناجح  🎉
- مربح  ↢ ( {pe}  💵 ) .
- نقاطك الحاليا  ↢ ( {kf}  💵 ) .
.</strong>""",parse_mode="html")
        else:
            pep = open(f"c{message.chat.id}.txt").read()
            with open(f"c{message.chat.id}.txt","r+")as fs:
                  fs.truncate(0)
            bot.reply_to(message,f"""<strong>
- لقد خسرت الحض  😬
- اموالك قبل  ↢ ( {pe} 💵 ) .
- اموالك الان  ↢ ( {pep} 💵 ) .
.</strong>""",parse_mode="html")
    if ms == "بخشيش":
          ca = open(f"blockTip.txt").read()
          if f"{message.chat.username}" in ca:
              bot.reply_to(message,f"<strong>So Quick!\nCome Here Again After 10m!</strong>",parse_mode="html")
          else:
              
              rt = randint(50,1000)
              ratb = rt
              acc = open(f"c{message.chat.id}.txt").read()
              ga = float(ratb) + float(acc)
              print(ratb)
              print(ga)
              with open(f"c{message.chat.id}.txt","r+")as fs:
                  fs.truncate(0)
              with open(f"c{message.chat.id}.txt","w")as va:
                  va.write(f"{ga}")
              bot.reply_to(message,f"<strong>💸 Your tip Is Available!🤩\n- You Got {ratb} 💵.\n- Your Balance Now its : {ga} 💵 .</strong>",parse_mode="html")
              with open(f"blockTip.txt","w")as df:
                 df.write(f"{message.chat.username}\n")
                 
                 df.close()
    if ms == "راتب":
          ca = open(f"block.txt").read()
          if f"{message.chat.username}" in ca:
              bot.reply_to(message,f"<strong>So Quick!\nCome Here Again After 10m!</strong>",parse_mode="html")
          else:
              list = ["programmer 💻-10000","King 🤴-100000","President 👨‍⚖-200000","Worker 🧑‍🔧-1000","Robot 🤖-2300","Driver 🚓-4000","DrogsSeller 🚬-1000000","GunSeller 🔫-90000","Pilot ✈️-30000","Captain 🛳-10000"]
              rt = random.choice(list)
              name = rt.split("-")[0]
              ratb = rt.split("-")[1]
              acc = open(f"c{message.chat.id}.txt").read()
              ga = float(ratb) + float(acc)
              print(ratb)
              print(ga)
              with open(f"c{message.chat.id}.txt","r+")as fs:
                  fs.truncate(0)
              with open(f"c{message.chat.id}.txt","w")as va:
                  va.write(f"{ga}")
              bot.reply_to(message,f"<strong>💸 عزيزي راتبك متاح🤩\n- لقد حصلت على : {ratb} 💵\n- مهنتك {name}.\n- Your رصيدك الان : {ga} 💵 .</strong>",parse_mode="html")
              with open(f"block.txt","w")as df:
                 df.write(f"{message.chat.username}\n")
                 df.close()
                 
@bot.callback_query_handler(func=lambda call: True)
def qwere(call):
    if call.data == "RebackBank":
        RebackBank(call.message)
    if call.data == "SpaceBank":
        SpaceBank(call.message)
    if call.data == "d":
        dell(call.message)

def dell(message):
    os.system(f"rm -rf {message.chat.id}.txt")
    print("ok")
def RebackBank(message):
    
    msg = message.text
    aw = glob.glob('./*.txt')
    if f"./{message.chat.id}.txt" in aw:
        bot.reply_to(message,f"<strong>Sorry You Already Have an Bank Account!</strong>",parse_mode="html")
    else:
        me = types.InlineKeyboardMarkup()
        me.row_width = 1
        me.add(ch3)
        chars = '1234567890'
        us = str(''.join((random.choice(chars) for i in range(15))))
        s = "5"+us
        try:
            with open(f"{message.chat.id}.txt","a")as x:
                x.write(f"name:{message.chat.first_name}:account:{s}:bank:RebackBank.")
                bot.reply_to(message,text=f"<strong>Done Create Banking Account! Account Detials :\nAccount Id : {s}\nBalance : 50 💵.\nBank Name : RebackBank.</strong>",parse_mode="html",reply_markup=me)
            with open(f"c{message.chat.id}.txt","a")as xs:
                xs.write("50")
                xs.close()
        except:
            pass
    
def SpaceBank(message):
    
    msg = message.text
    aw = glob.glob('./*.txt')
    if f"./{message.chat.id}.txt" in aw:
        bot.reply_to(message,f"<strong>Sorry You Already Have an Bank Account!</strong>",parse_mode="html")
    else:
        me = types.InlineKeyboardMarkup()
        me.row_width = 1
        me.add(ch3)
        chars = '1234567890'
        us = str(''.join((random.choice(chars) for i in range(15))))
        s = "5"+us
        try:
            with open(f"{message.chat.id}.txt","a")as x:
                x.write(f"name:{message.chat.first_name}:account:{s}:bank:SpaceBank.")
                bot.reply_to(message,text=f"<strong>تم انشاء حسابك البنكي! تفاصيل الحساب:\nمعرف الحساب : {s}\nالرصيد : 50 💵.\nاسم البنك : Tomebank.</strong>",parse_mode="html",reply_markup=me)
            with open(f"c{message.chat.id}.txt","a")as xs:
                xs.write("50")
                xs.close()
        except:
            pass
print('starte')           
bot.infinity_polling()
