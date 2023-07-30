import pyrogram
import re
import json
import pymysql
from pyrogram import Client
import pyromod
import mysql.connector
from pyromod import listen
from pyrogram.types import*
from pyrogram.types import ReplyKeyboardMarkup , InlineKeyboardButton , KeyboardButton
from pyrogram import filters
from pyrogram.types import Message
import requests
import time
import asyncio
import random
from flask import Flask,redirect,url_for,render_template,request
from requests import post , get
from datetime import datetime, timedelta
#-------------------------------Bot Information---------------------------#
bot = Client(
    name="Turbo",
    api_id=23384444,
    api_hash="c21921fc5b43a730cf7c3c1cc6ae8573",
    bot_token="6180212565:AAHwqf1Jei7AFtO3XT3L_0DLtN0ZPV7lsy8"
    )

list_admin = [6610344575]
list_number = []
list_link = []
list_number_panel2 = []
list_link_panel2 = []
list_number_panel3 = []
list_link_panel3 = []
list_number_panel4 = []
list_link_panel4 = []
status_list = []
status_list_panel2 = []
status_list_panel3 = []
status_list_panel4 = []
list_ticket = []
money_num =[]
money_num_panel2 = []
money_num_panel3 = []
money_num_panel4 = []
country_list = []
sell_num = []
sell_link = []
list_eror = []
list_chanel = []
list_link_channel = []
keyboard_option = [["پنل اول👑"],[],[],[],["راهنما📄","back🔙"]]
head= {
  'User-Agent': 'PostmanRuntime/7.26.8',
  'Content-Type': 'application/x-www-form-urlencoded'
}
#-------------------------------------------------------------------------#
#----------------------------Bot Database--------------------------------#

host = "localhost"
database = "pnlturbo_botuser"#
user = "pnlturbo_root" 
password = "Root1botuser" 
con = mysql.connector.connect(
    host=host,
    database=database,
    user=user,
    password=password)

if con.is_connected():
    print("ok")
else:
    print("Not ok")
    con.close()
cur = con.cursor()



#     print("ok create")  
# else:
#     print("Cant connect database")
# connection.close()

#----------------------------check join----------------------------------#
#----------------------------Bot Check Join Channel--------------------------------#
async def checkjoin(__,client,message):
    userid = message.from_user.id
    if len(list_chanel) == 0 :
        return True
    else:
        if len(list_chanel) <= 1:
            try:
                cha = await client.get_chat_member(
                    chat_id=f"{list_chanel[0]}",
                    user_id= userid
                )
                mms = cha
                if mms in ['admin','creator','member']:
                    return True 
                else:
                    await Main(client , message)
                    return False
            except:
                text = "💢 دوست گرامی برای ادامه استفاده از خدمات ربات باید در کانال های  زیر عضو شوید 💢"
                await bot.send_message(
                    userid,
                    text, 
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton(f"{list_chanel[0]}",url=f"{list_link_channel[0]}")]]
                    ))
                return False
        else:
            if len(list_chanel) <= 2:
                try :
                    for x in list_chanel :
                        m = await client.get_chat_member(
                            chat_id = f"{x}",
                            user_id = userid
                        )
                        if m in ['admin','creator','member']:
                            return True 
                        else:
                            await Main(client , message)
                            return False
                except:
                    text = "💢 دوست گرامی برای ادامه استفاده از خدمات ربات باید در کانال های  زیر عضو شوید 💢"
                    await bot.send_message(
                        userid,
                        text, 
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton(f"{list_chanel[0]}",url=f"{list_link_channel[0]}")],
                            [InlineKeyboardButton(f"{list_chanel[1]}", url=f"{list_link_channel[1]}")]]
                        ))
                    return False
            else:
                if len(list_chanel) <= 3:
                    try :
                        for x in list_chanel :
                            m = await client.get_chat_member(
                                chat_id = f"{x}",
                                user_id = userid
                            )
                            n = m 
                            if n in ['admin','creator','member']:
                                return True 
                            else:
                                await Main(client , message)
                                return False
                    except:
                        text = "💢 دوست گرامی برای ادامه استفاده از خدمات ربات باید در کانال های  زیر عضو شوید 💢"
                        await bot.send_message(
                            userid,
                            text, 
                            reply_markup=InlineKeyboardMarkup(
                                [[InlineKeyboardButton(f"{list_chanel[0]}",url=f"{list_link_channel[0]}")],
                                [InlineKeyboardButton(f"{list_chanel[1]}", url=f"{list_link_channel[1]}")],
                                [InlineKeyboardButton(f"{list_chanel[2]}",url=f"{list_link_channel[2]}")]]
                            ))
                        return False
                else:
                    if len(list_chanel) <= 4:
                        try :
                            for x in list_chanel :
                                m = await client.get_chat_member(
                                    chat_id = f"{x}",
                                    user_id = userid
                                )
                                n = m 
                                if n in ['admin','creator','member']:
                                    return True 
                                else:
                                    await Main(client , message)
                                    return False
                        except:
                            text = "💢 دوست گرامی برای ادامه استفاده از خدمات ربات باید در کانال های  زیر عضو شوید 💢"
                            await bot.send_message(
                                userid,
                                text, 
                                reply_markup=InlineKeyboardMarkup(
                                    [[InlineKeyboardButton(f"{list_chanel[0]}",url=f"{list_link_channel[0]}")],
                                    [InlineKeyboardButton(f"{list_chanel[1]}", url=f"{list_link_channel[1]}")],
                                    [InlineKeyboardButton(f"{list_chanel[2]}",url=f"{list_link_channel[2]}")],
                                    [InlineKeyboardButton(f"{list_chanel[3]}",url=f"{list_link_channel[3]}")]]
                                ))
                            return False
                    else:
                        if len(list_chanel) <= 5:
                            try :
                                for x in list_chanel :
                                    m = await client.get_chat_member(
                                        chat_id = f"{x}",
                                        user_id = userid
                                    )
                                    n = m 
                                    if n in ['admin','creator','member']:
                                        return True 
                                    else:
                                        await Main(client , message)
                                        return False
                            except:
                                text = "دوست گرامی برای استفاده از خدمات باید در کانال ما عضو شوید :\n@PARSA_ELF\n بعد از عضویت ربات رو استارت کنید\n/start"
                                await bot.send_message(
                                    userid,
                                    text, 
                                    reply_markup=InlineKeyboardMarkup(
                                        [[InlineKeyboardButton(f"{list_chanel[0]}",url=f"{list_link_channel[0]}")],
                                        [InlineKeyboardButton(f"{list_chanel[1]}", url=f"{list_link_channel[1]}")],
                                        [InlineKeyboardButton(f"{list_chanel[2]}",url=f"{list_link_channel[2]}")],
                                        [InlineKeyboardButton(f"{list_chanel[3]}",url=f"{list_link_channel[3]}")],
                                        [InlineKeyboardButton(f"{list_chanel[4]}",url=f"{list_link_channel[4]}")]]
                                    ))
                                return False
                        else:
                            pass
            

check_member_filter = filters.create(checkjoin)
#-------------------------------------------------------------------------#


#----------------------------Bot Main------------------------------------#
@bot.on_message(check_member_filter)
async def Main(client , message):
    text = message.text
    chat_id = message.chat.id
    user_id = message.from_user.id
    if text == "/start":
        await Start(message , con , cur , get_balance , update_balance)
    if text == "🗂تامین کننده ها":
        if user_id in list_admin :
            await tamin(message)    
    if text == "🧾پشتیبانی":
        if user_id in list_admin :
            await supportad(message , list_ticket)
    if text == "پیام همگانی📣":
        if user_id in list_admin :
            await textall(message)
    if text == "show info📜":
        if user_id in list_admin :
            qw = ReplyKeyboardMarkup(keyboard=[
                ["telegram","number"],
                ["back🔙"]
            ], resize_keyboard=True)
            await bot.send_message(message.chat.id , text="یکی از گزینه های زیر را نتخاب نمایید :\n\n💢 توجه داشته باشید که درصورت انتخاب گزینه\n<telegram>\nباید ایدی تلگرام کاربر یعنی ایدی @ را برای ما ارسال کنید و درصورت انتخاب گزینه \n<number>\nباید ایدی عددی کاربر را ارسال نمایید.💢", reply_markup=qw)
            
    if text == "telegram":
        if user_id in list_admin :
            q = await bot.ask(message.chat.id , text="👤 آیدی تلگرامی کاربر موردنظر خود را وارد نمایید")
            qt = q.text
            lkj = await bot.get_users(f"{qt}")
            lkji = lkj.id
            cur.execute(f"SELECT Balance , number , phone FROM userbot WHERE userid = {lkji}")
            resualt_all = cur.fetchone()
            if resualt_all :
                Balance1 = resualt_all[0]
                number1 = resualt_all[1]
                phone4 = resualt_all[2]
                cur.execute(f"SELECT number , phone FROM userbot WHERE userid = {lkji}")
                resualt_3 = cur.fetchone()          
                if resualt_3 == ('0','0') :
                    a = "سفارشی در وضعیت باز قرار ندارد ❌"

                    await bot.send_message(message.chat.id , text=f"📄 اطلاعات کاربر {qt} :\n\n📧 آیدی عددی : {lkji}\n💰 مقدار موجودی : {Balance1}💎\n🛍 وضعیت سفارش : {a}\n\n💢 قیمت هر 💎 معادل هزارتومان میباشد")
                else:
                    await bot.send_message(message.chat.id , text=f"📄 اطلاعات کاربر {qt} :\n\n📧 آیدی عددی : {lkji}\n💰 مقدار موجودی : {Balance1}💎\n🛍 وضعیت سفارش : درحال بررسی لطفا منتظر بمانید 🔄\n\n💢 قیمت هر 💎 معادل هزارتومان میباشد")
                    
                    for x in resualt_3 :
                        if x == '0':
                            pass
                        else:
                            cur.execute(f"SELECT phon , tocken FROM userbot WHERE userid = {lkji}")
                            resualt_number = cur.fetchone()
                            if resualt_number != ('0','0') :
                                phone5 = resualt_number[0]
                                await bot.send_message(message.chat.id , text=f"📲 شماره مجازی : {phone5}\n📱 پلتفرم : تلگرام\n کشور : امریکا 🇺🇸\nدرحال خرید")
                            else:
                                cur.execute(f"SELECT phone , token FROM userbot WHERE userid = {lkji}")
                                resualt_token = cur.fetchone()
                                if resualt_token != ('0','0') :
                                    phone6 = resualt_token[0]
                                    await bot.send_message(message.chat.id , text=f"📲 شماره مجازی : {phone6}\n📱 پلتفرم : تلگرام\n کشور : امریکا 🇺🇸\nدرحال خرید")

    if text == "number":
        lkj = await bot.ask(message.chat.id , text="👤 آیدی عددی کاربر را وارد نمایید")
        lkjj = lkj.text
        cur.execute(f"SELECT Balance , number , phone FROM userbot WHERE userid = {lkjj}")
        resualt_all = cur.fetchone()
        if resualt_all :
            Balance1 = resualt_all[0]
            number1 = resualt_all[1]
            phone4 = resualt_all[2]
            cur.execute(f"SELECT number , phone FROM userbot WHERE userid = {lkjj}")
            resualt_3 = cur.fetchone()          
            if resualt_3 == ('0','0') :
                a = "سفارشی در وضعیت باز قرار ندارد ❌"

                await bot.send_message(message.chat.id , text=f"📄 اطلاعات کاربر {lkjj} :\n\n📧 آیدی عددی : {lkjj}\n💰 مقدار موجودی : {Balance1}💎\n🛍 وضعیت سفارش : {a}\n\n💢 قیمت هر 💎 معادل هزارتومان میباشد")
            else:
                await bot.send_message(message.chat.id , text=f"📄 اطلاعات کاربر {lkjj} :\n\n📧 آیدی عددی : {lkjj}\n💰 مقدار موجودی : {Balance1}💎\n🛍 وضعیت سفارش : درحال بررسی لطفا منتظر بمانید 🔄\n\n💢 قیمت هر 💎 معادل هزارتومان میباشد")
                
                for x in resualt_3 :
                    if x == '0':
                        pass
                    else:
                        cur.execute(f"SELECT phon , tocken FROM userbot WHERE userid = {lkjj}")
                        resualt_number = cur.fetchone()
                        if resualt_number != ('0','0') :
                            phone5 = resualt_number[0]
                            await bot.send_message(message.chat.id , text=f"📲 شماره مجازی : {phone5}\n📱 پلتفرم : تلگرام\n کشور : امریکا 🇺🇸\nدرحال خرید")
                        else:
                            cur.execute(f"SELECT phone , token FROM userbot WHERE userid = {lkjj}")
                            resualt_token = cur.fetchone()
                            if resualt_token != ('0','0') :
                                phone6 = resualt_token[0]
                                await bot.send_message(message.chat.id , text=f"📲 شماره مجازی : {phone6}\n📱 پلتفرم : تلگرام\n کشور : امریکا 🇺🇸\nدرحال خرید")                           
            
                        
                                            
                                
            
    if text == "🔋افزایش موجودی":
        if user_id in list_admin :
            await admony(message)
    if text == "👀show admin":
        if user_id in list_admin :
            await bot.send_message(chat_id , text=f"👨‍💻admin set:\n{list_admin}")
    if text == "راهنما📄":
        await bot.send_message(message.chat.id , text="🔰 کاربر عزیز به بخش راهنما خوش اومدید ...\n\nدرنظر داشته باشید نکات زیر در حین خرید شما کاملا مهم میباشند ‼️\n\n1⃣ قبل از خرید خود حتما با استفاده از گزینه \n<< استعلام قیمت💰 >>\nاز قیمت فعلی پنل های فروش و کشور انتخاب شده برای فروش با خبر بشید❕\n2⃣ برای خرید شما اکانت زن های عزیز دو پنل تامین کننده در نظر گرفته شده است که درصورت انتخاب یکی از پنل ها شما وارد مرحله خرید میشوید ❕\n3⃣ درصورتی که هر دو پنل خرید غیرفعال بود حتما منتظر بمانید تا درگاه فروش توسط پشتیبانان ما باز شود ❕\n4⃣ در حین خرید شما نمیتوانید سفارش خود را لغو کنید مگر اینکه ربات رسید سفارش را برای شما ارسال کند و سه تا گزینه \n<< کد مجدد🔄 >>\n<< لغو سفارش❌ >>\n<< تکمیل سفارش✅ >>\nبرای شما نمایان شود\n5⃣ در حین خرید بعد از دریافت شماره از ربات . درصورتی که ربات به شما کد ورود را بدهد شما 180 ثانیه فرصت دارید تا سفارش خود را با ارسال پیام\n<< تکمیل سفارش✅ >>\nتکمیل نمایید و یا از گزینه های دیگر استفاده نمایید\n6⃣ درصورتی که سفارش خود را بعد از 180 ثانیه تکمیل نکنید ربات بصورت خودکار سفارش شما را به تامین کننده تکمیل اعلام میکند و مبلغ تعیین شده از حساب شما کسر میشود ❕\n7⃣ درصورتی که سفارشی در وضعیت باز داشته باشید و تایم سفارش به پایان نرسیده باشد میتوانید با ارسال پیام\n<< 🪪اطلاعات اکانت >>\nاز شماره سفارش خود و یا شماره خریداری شده با خبر بشید و با ارساال پیام های دیگر سفارش خود را پیش ببرید ❕\n\n💢 هر نکته و سوالی که داشتید با ثبت تیکت پشتیبانی میتوانید با پشتیبانان ما ارتباط برقرار کنید 💢")
    if text == "💫کانال ها":
        if user_id in list_admin :
            if len(list_chanel) != 5:
                po = await bot.ask(message.chat.id , text="💢 آیا میخواهید کانال جدید اضافه کنید؟\nyes/no")
                pot = po.text
                if pot == "yes":
                    qw = await bot.ask(message.chat.id , text="💢 توجه فرمایید برای اضافه کردن کانال باید قبل از اضافه کردن کانال مورد نظر به لیست ربات را در ان کانال عضو و به عنوان ادمین تعریف کنید 💢\n\n💢 توجه فرمایید بعد از تایید این بخش ربات لیست کانال ها را ریست کرده و شما میتوانید کانال ها را به لیست اضافه کنید 💢\nبرای تایید این بخش yes را ارسال کنید در غیراینصورت no را بفرستید")
                    qwt = qw.text
                    if qwt == "yes":
                        list_chanel.clear()
                        list_link_channel.clear()
                        await bot.send_message(message.chat.id , text="لیست کانال ها با موفقیت ریست شد ✅")
                        m = await bot.ask(chat_id , text="آیا قصد اضافه کردن کانال دارید ⁉️\n🔰شماره کانال 1\nفقط با yes یا no جواب دهید")
                        mt = m.text
                        if mt == "yes":
                            q = await bot.ask(message.chat.id , text="🔰 آید کانال را همراه با @ وارد نمایید")
                            qt = q.text
                            if qt != "no":
                                list_chanel.append(qt)
                                w = await bot.ask(chat_id , text="🔰 لینک کانال را وارد نمایید")
                                wt = w.text
                                list_link_channel.append(wt)
                                r = await bot.ask(chat_id , text=f"🔰 کانال اول تایید شد ✅\n\n📜 اطلاعات کانال 1 :\n📝آیدی : {qt}\n🔒 لینک کانال : {wt}\n\nآیا قصد اضافه کردن کانال دارید ⁉️\n🔰شماره کانال 2\nفقط با yes یا no جواب دهید")
                                rt = r.text
                                if rt == "yes":
                                    e = await bot.ask(chat_id , text="🔰 آید کانال را همراه با @ وارد نمایید")
                                    et = e.text
                                    list_chanel.append(et)
                                    t = await bot.ask(chat_id , text="🔰 لینک کانال را وارد نمایید")
                                    tt = t.text
                                    list_link_channel.append(tt)
                                    y = await bot.ask(chat_id , text=f"🔰 کانال دوم تایید شد ✅\n\n📜 اطلاعات کانال 2 :\n📝آیدی : {et}\n🔒 لینک کانال : {tt}\n\nآیا قصد اضافه کردن کانال دارید ⁉️\n🔰شماره کانال 3\nفقط با yes یا no جواب دهید")
                                    yt = y.text
                                    if yt == "yes":
                                        u = await bot.ask(chat_id , text="🔰 آید کانال را همراه با @ وارد نمایید")
                                        ut = u.text
                                        list_chanel.append(ut)
                                        q = await bot.ask(chat_id , text="🔰 لینک کانال را وارد نمایید")
                                        qt = q.text
                                        list_link_channel.append(qt)
                                        w = await bot.ask(chat_id , text=f"🔰 کانال سوم تایید شد ✅\n\n📜 اطلاعات کانال 3 :\n📝آیدی : {ut}\n🔒 لینک کانال : {qt}\n\nآیا قصد اضافه کردن کانال دارید ⁉️\n🔰شماره کانال 4\nفقط با yes یا no جواب دهید")
                                        wt = w.text
                                        if wt == "yes":
                                            r = await bot.ask(chat_id , text="🔰 آید کانال را همراه با @ وارد نمایید")
                                            rt = r.text
                                            list_chanel.append(rt)
                                            a = await bot.ask(chat_id , text="🔰 لینک کانال را وارد نمایید")
                                            at = a.text
                                            list_link_channel.append(at)
                                            b = await bot.ask(chat_id , text=f"🔰 کانال چهارم تایید شد ✅\n\n📜 اطلاعات کانال 4 :\n📝آیدی : {rt}\n🔒 لینک کانال : {at}\n\nآیا قصد اضافه کردن کانال دارید ⁉️\n🔰شماره کانال 5\nفقط با yes یا no جواب دهید")
                                            bt = b.text
                                            if bt == "yes":
                                                p = await bot.ask(chat_id , text="🔰 آید کانال را همراه با @ وارد نمایید")
                                                pt = p.text
                                                list_chanel.append(pt)
                                                l = await bot.ask(chat_id , text="🔰 لینک کانال را وارد نمایید")
                                                lt = l.text
                                                list_link_channel.append(lt)
                                                await bot.send_message(chat_id , text="محدودیت برای کانال ها تایید شد ✅\n🌐 5 کانال برای محدودیت تعیین شد",reply_markup=InlineKeyboardMarkup(
                                                    [[InlineKeyboardButton(f"{list_chanel[0]}",url=f"{list_link_channel[0]}")],
                                                    [InlineKeyboardButton(f"{list_chanel[1]}",url=f"{list_link_channel[1]}")],
                                                    [InlineKeyboardButton(f"{list_chanel[2]}",url=f"{list_link_channel[2]}")],
                                                    [InlineKeyboardButton(f"{list_chanel[3]}",url=f"{list_link_channel[3]}")],
                                                    [InlineKeyboardButton(f"{list_chanel[4]}",url=f"{list_link_channel[4]}")]]
                                                ))
                                            else:
                                                await bot.send_message(chat_id , text="محدودیت برای کانال ها تایید شد ✅\n🌐 4 کانال برای محدودیت تعیین شد",reply_markup=InlineKeyboardMarkup(
                                                    [[InlineKeyboardButton(f"{list_chanel[0]}",url=f"{list_link_channel[0]}")],
                                                    [InlineKeyboardButton(f"{list_chanel[1]}",url=f"{list_link_channel[1]}")],
                                                    [InlineKeyboardButton(f"{list_chanel[2]}",url=f"{list_link_channel[2]}")],
                                                    [InlineKeyboardButton(f"{list_chanel[3]}",url=f"{list_link_channel[3]}")]]
                                                ))
                                        else:
                                            await bot.send_message(chat_id , text="محدودیت برای کانال ها تایید شد ✅\n🌐 3 کانال برای محدودیت تعیین شد",reply_markup=InlineKeyboardMarkup(
                                                    [[InlineKeyboardButton(f"{list_chanel[0]}",url=f"{list_link_channel[0]}")],
                                                    [InlineKeyboardButton(f"{list_chanel[1]}",url=f"{list_link_channel[1]}")],
                                                    [InlineKeyboardButton(f"{list_chanel[2]}",url=f"{list_link_channel[2]}")]]
                                                ))
                                    else:
                                        await bot.send_message(chat_id , text="محدودیت برای کانال ها تایید شد ✅\n🌐 2 کانال برای محدودیت تعیین شد",reply_markup=InlineKeyboardMarkup(
                                                [[InlineKeyboardButton(f"{list_chanel[0]}",url=f"{list_link_channel[0]}")],
                                                [InlineKeyboardButton(f"{list_chanel[1]}",url=f"{list_link_channel[1]}")]]
                                            ))
                                else:
                                    await bot.send_message(chat_id , text="محدودیت برای کانال ها تایید شد ✅\n🌐 1 کانال برای محدودیت تعیین شد",reply_markup=InlineKeyboardMarkup(
                                            [[InlineKeyboardButton(f"{list_chanel[0]}",url=f"{list_link_channel[0]}")]]
                                        ))
                            else:
                                await bot.send_message(chat_id , text="💢 عملیات لغو شد")
                        else:
                            await bot.send_message(chat_id , text="💢 عملیات لغو شد")
                    else:
                        await bot.send_message(chat_id , text="💢 عملیات لغو شد")
                else:
                    await bot.send_message(chat_id , text="💢 عملیات لغو شد")
            else:             
                await bot.send_message(message.chat.id , text="تعداد کانال ها به 5 عدد رسیده و امکان اضافه کردن کانال جدید نیست ⛔️")
                m = await bot.ask(message.chat.id , text="💢 آیا میخواهید لیست کانال ها را ریست کنید ؟ \nyes/no")
                mt = m.text
                if mt == "yes":
                    list_chanel.clear()
                    list_link_channel.clear()
                    await bot.send_message(message.chat.id , text="عملیات با موفقیت انجام شد ✅")
                else:
                    await bot.send_message(message.chat.id , text="💢 عملیات لغو شد")
        
    if text == "👨‍💻add admin":
        if user_id in list_admin :
            ad = await bot.ask(chat_id, text="🔰 for add admin, please send id telegram with @")
            adi = ad.text
            #print(adi)
            a123 = await bot.get_users(f"{adi}")
            aid = a123.id 
            #print(aid)
            if aid in list_admin :
                await bot.send_message(chat_id , text=f"💢 آیدی وارد شده قبلا به عنوان ادمین در ربات تعریف شده است")
            else:
                list_admin.append(aid)
                await bot.send_message(chat_id , text=f"آیدی وارد شده به عنوان ادمین در ربات اضافه شد ✅")
                await bot.send_message(chat_id=aid , text=f"تبریک !. شما ادمین شدید ✅\n\nربات را /start کنید تا تعییرات اعمال شوند.")
    if text == "❌Delete admin":
        if user_id in list_admin :
            de = await bot.ask(chat_id , text=f"🔰 for delete admin , please send id telegram with @")
            dele = de.text
            d = await bot.get_users(f"{dele}")
            did = d.id
            list_admin.remove(did)
            await bot.send_message(chat_id, text="آیدی وارد شده از مدیریت حذف شد ✅")
    if text == "💸افزایش موجودی":
        button1 = InlineKeyboardButton("50 هزارتومان 💎50", callback_data="50")
        button2 = InlineKeyboardButton("100 هزارتومان 💎100", callback_data="100")
        button3 = InlineKeyboardButton("150 هزارتومان 💎150", callback_data="150")
        button4 = InlineKeyboardButton("200 هزارتومان 💎200", callback_data="200")
        cloum1 = [button1 , button2]
        cloum2 = [button3 , button4]
        cloums = [cloum1 , cloum2]
        await bot.send_message(chat_id , "💢 لطفا یکی از گزینه های زیر را انتخاب کنید", reply_markup=InlineKeyboardMarkup(cloums))
    if text == "🪪اطلاعات اکانت":
        cur.execute(f"SELECT  number , phone FROM userbot WHERE userid = {user_id}")
        resualt_info = cur.fetchone()
        cur.execute(f"SELECT Balance FROM userbot WHERE userid = {user_id}")
        resualt_balance = cur.fetchone()
        balance_re = int(resualt_balance[0])
        number_1 = resualt_info[0]
        phone_1 = resualt_info[1]
        if resualt_info == ('0','0') :
            cur.execute(f"SELECT Balance FROM userbot WHERE userid = {user_id}")
            resualt_balance = cur.fetchone()
            balance_re = int(resualt_balance[0])
            await bot.send_message(message.chat.id , text=f"اطلاعات اکانت شما ...\n\n📛 اسم شما : {message.from_user.first_name}\n🆔 آیدی عددی : {user_id}\n💰 مقدار موجودی : {balance_re}💎\n🛍 سفارشی در وضعیت باز وجود ندارد")
        else:
            for y in resualt_info :
                if y == '0':
                    pass
                    #print("y = 0",y)
                else:
                    cur.execute(f"SELECT phon , tocken FROM userbot WHERE userid = {user_id}")
                    resualt_1 = cur.fetchone()
                    if resualt_1 != ('0','0') :
                        await bot.send_message(message.chat.id , text=f"اطلاعات اکانت شما ...\n\n📛 اسم شما : {message.from_user.first_name}\n🆔 آیدی عددی : {user_id}\n💰 مقدار موجودی : {balance_re}💎\n🛍 شماره پیگیری سفارش : {number_1}\n\n توجه : \nسفارش با شماره پیگیری {number_1} تا 100 ثانیه ⏰ دیگر بصورت خودکار تکمیل میشود و مبلغ ان از حساب شما کسر میشود . ❗️ \n💢 لذا خواهشمندیم درصورتی که اکانت تلگرام را بر روی شماره دریافتی ساختید , سفارش خودتون رو با ارسال پیام << ✅تکمیل سفارش >> پایان دهید در غیر اینصورت از پیام های << 🔄کد مجدد >> و << ❌لغو سفارش >> استفاده کنید 💢")
                    else:
                        if phone_1 != '0':
                            await bot.send_message(message.chat.id , text=f"اطلاعات اکانت شما ...\n\n📛 اسم شما : {message.from_user.first_name}\n🆔 آیدی عددی : {user_id}\n💰 مقدار موجودی : {balance_re}💎\n🛍 شماره پیگیری سفارش : {phone_1}\n\n توجه : \nسفارش با شماره پیگیری {phone_1} تا 100 ثانیه ⏰ دیگر بصورت خودکار تکمیل میشود و مبلغ ان از حساب شما کسر میشود . ❗️ \n💢 لذا خواهشمندیم درصورتی که اکانت تلگرام را بر روی شماره دریافتی ساختید , سفارش خودتون رو با ارسال پیام << ✅تکمیل سفارش >> پایان دهید در غیر اینصورت از پیام های << 🔄کد مجدد >> و << ❌لغو سفارش >> استفاده کنید 💢")
                                
    if text == "back🔙":
        await Start(message , con , cur , get_balance , update_balance)
    if text == "کاهش موجودی🪫":
        q = await bot.ask(message.chat.id , text="تعیین کنید با استفاده از << آیدی عددی >> و یا << آیدی تلگرام >>  \n you must send message << آیدی عددی >> or << آیدی تلگرام >>")
        qt = q.text
        if qt == "آیدی تلگرام":
            poi = await bot.ask(message.chat.id , text=f"👤 آیدی تلگرام را وارد نمایید")
            poit = poi.text
            az = await bot.get_users(f"{poit}")
            azi = az.id 
            cur.execute(f"SELECT Balance FROM userbot WHERE userid = {azi}")
            ew = cur.fetchone()
            if ew :
                balance = ew[0]
                if balance != None :
                    await bot.send_message(message.chat.id , text=f"📜 اطلاعات اکانت {poit} :\n\n👤 ایدی کاربر : {azi}\n💰 موجودی فعلی : {balance}💎\n\n💢 توجه قیمت هر 💎 معادل هزارتومان میباشد 💢")
                    lk = await bot.ask(message.chat.id , text=f"🔰 مقدار 💎 که میخواهید از حساب کاربر کسر کنید \n\n💢 توجه باید این مقدار را فقط یک عدد لاتین وارد نمایید و درصورتی که میخواهید این عملیات لغو شود باید no را ارسال نمایید💢")
                    lki = lk.text
                    if lki != "no":
                        new = int(balance) - int(lki)
                        if new < 0 :
                            await bot.send_message(message.chat.id , text=f"❌ تراکنش ناموفق ❌ : \n\n💢 مقدار 💎 که میخواهید از بالانس کاربر کم کنید بیشتر از مقدار موجودی بالانس کاربر میباشد 💢")
                            await Start(message , con , cur , get_balance , update_balance)
                        else:
                            params = (new , azi)
                            cur.execute("UPDATE userbot SET Balance = %s WHERE userid = %s",params)
                            con.commit()
                            await bot.send_message(message.chat.id , text=f"📜 تراکنش موفق :\n\n👤 آیدی تلگرام : {poit}\n📝 آیدی عددی : {azi}\n🪫 تعداد 💎 کاهش خورده : {lki}\n💰 موجودی فعلی : {new}💎")
                            await Start(message , con , cur , get_balance , update_balance)
                    else:
                        await bot.send_message(message.chat.id , text="💢 عملیات با موفقیت لغو شد")
                        await Start(message , con , cur , get_balance , update_balance)
                else:
                    await bot.send_message(message.chat.id , text="💢 عملیات لغو شد \nکاربری با این اطلاعات وجود ندارد ❌")
                    await Start(message , con , cur , get_balance , update_balance)
            else:
                await bot.send_message(message.chat.id , text="💢 عملیات لغو شد \nکاربری با این اطلاعات وجود ندارد ❌")
                await Start(message , con , cur , get_balance , update_balance)
        elif qt == "آیدی عددی" :
            poi3 = await bot.ask(message.chat.id , text=f"👤 آیدی عددی تلگرام را وارد نمایید")
            poit3 = poi3.text
            cur.execute(f"SELECT Balance FROM userbot WHERE userid = {poit3}")
            peiy = cur.fetchone()
            if peiy :
                balance2 = peiy[0]
                if balance2 != None:
                    await bot.send_message(message.chat.id , text=f"📜 اطلاعات اکانت {poit3} :\n\n👤 ایدی کاربر : {poit3}\n💰 موجودی فعلی : {balance2}💎\n\n💢 توجه قیمت هر 💎 معادل هزارتومان میباشد 💢")
                    lk = await bot.ask(message.chat.id , text=f"🔰 مقدار 💎 که میخواهید از حساب کاربر کسر کنید \n\n💢 توجه باید این مقدار را فقط یک عدد لاتین وارد نمایید و درصورتی که میخواهید این عملیات لغو شود باید no را ارسال نمایید💢")
                    lki = lk.text
                    if lki != "no":
                        new = int(balance2) - int(lki)
                        if new < 0 :
                            await bot.send_message(message.chat.id , text=f"❌ تراکنش ناموفق ❌ : \n\n💢 مقدار 💎 که میخواهید از بالانس کاربر کم کنید بیشتر از مقدار موجودی بالانس کاربر میباشد 💢")
                            await Start(message , con , cur , get_balance , update_balance)
                        else:
                            params = (new , poit3)
                            cur.execute("UPDATE userbot SET Balance = %s WHERE userid = %s",params)
                            con.commit()
                            await bot.send_message(message.chat.id , text=f"📜 تراکنش موفق :\n\n👤 آیدی تلگرام : {poit3}\n📝 آیدی عددی : {poit3}\n🪫 تعداد 💎 کاهش خورده : {lki}\n💰 موجودی فعلی : {new}💎")
                            await Start(message , con , cur , get_balance , update_balance)
                    else:
                        await bot.send_message(message.chat.id , text="💢 عملیات با موفقیت لغو شد")
                        await Start(message , con , cur , get_balance , update_balance)
                else:
                    await bot.send_message(message.chat.id , text="💢 عملیات لغو شد \nکاربری با این اطلاعات وجود ندارد ❌")
                    await Start(message , con , cur , get_balance , update_balance)
            else:
                await bot.send_message(message.chat.id , text="💢 عملیات لغو شد \nکاربری با این اطلاعات وجود ندارد ❌")
                await Start(message , con , cur , get_balance , update_balance)
        else:
            await bot.send_message(message.chat.id , text="💢 عملیات لغو شد")
            await Start(message , con , cur , get_balance , update_balance)
    if text == "🧑‍💻پشتیبانی":
        await support(message , list_ticket)
    if text == "📄لیست کاربران":
        if user_id in list_admin :
            piuy = ReplyKeyboardMarkup(keyboard=[
                ["نمایش ایدی ها👀"],
                ["حذف ایدی ها📛"],
                ["back🔙"]
            ], resize_keyboard=True)
            await bot.send_message(message.chat.id , text="یکی از گزینه های زیر را انتخاب نمایید 🙂", reply_markup=piuy)
    if text == "نمایش ایدی ها👀":
        if user_id in list_admin :
            await bot.send_message(chat_id=message.chat.id , text=f"👀 نمایش کاربرانی که تیکت ارسال کردنند و 💢 پاسخی دریافت نکردنند ...\n\n{list_ticket}")
    if text == "📖کاربران":
        if user_id in list_admin :
            cur.execute("SELECT userid FROM userbot")
            resualt_users1 = cur.fetchall()
            await bot.send_message(message.chat.id , text=f"{resualt_users1}")
    if text == "حذف ایدی ها📛":
        if user_id in list_admin :
            list_ticket.clear()
            await bot.send_message(chat_id=message.chat.id , text="لیست تیکت ها ریست شد ✔\n\nتمامی آیدی عددی ها حذف شدنند ❗️")
    if text == "📝ارسال جواب":
        if user_id in list_admin :
            await ans(message , list_ticket)
    if text == "تعیین قیمت💲":
        if user_id in list_admin :
            if not bool(money_num) and not bool(money_num_panel2) and not bool(money_num_panel3) and not bool(money_num_panel4):
                await bot.send_message(message.chat.id , text="‼️ قیمت فعلی برای شماره ها تعیین نشده است ‼️")
                lk = await bot.ask(message.chat.id , text="🔰 قیمت را برای پنل های فروش خود تعیین نمایید .\n\n💢 توجه : شما میتوانید با ارسال پیام های << پنل اول >> و << پنل دوم >> و << پنل سوم >> و << پنل چهارم >> قیمت را برای هر پنل تعیین کنید 💢\n\nدرنظر داشته باشید باید قیمت را حتما عدد ارسال کنید ❕")
                if lk is None :
                    await bot.send_message(message.chat.id , text="‼️ قیمتی تعیین نشد ‼️")
                else:
                    lkt = lk.text
                    if lkt == "پنل اول" :
                        po = await bot.ask(message.chat.id , text="پنل اول تایید شد ✅\n\n💢 قیمت را حتما به عدد ارسال نمایید 💢")
                        pot = po.text
                        money_num.append(f"{pot}")
                        await bot.send_message(message.chat.id , text=f"قیمت تعیین شد ✅\n\n📲 شماره امریکا {pot}💎")
                    else:
                        if lkt == "پنل دوم" :
                            po1 = await bot.ask(message.chat.id , text="پنل دوم تایید شد ✅\n\n💢 قیمت را حتما به عدد ارسال نمایید 💢")
                            po1t = po1.text
                            money_num_panel2.append(f"{po1t}")
                            await bot.send_message(message.chat.id , text=f"قیمت تعیین شد ✅\n\n📲 شماره امریکا {po1t}💎")
                        else:
                            if lkt == "پنل سوم":
                                po3 = await bot.ask(message.chat.id , text="پنل سوم تایید شد ✅\n\n💢 قیمت را حتما به عدد ارسال نمایید 💢")
                                po3t = po1.text
                                money_num_panel3.append(f"{po3t}")
                                await bot.send_message(message.chat.id , text=f"قیمت تعیین شد ✅\n\n📲 شماره امریکا {po3t}💎")
                            else:
                                if lkt == "پنل چهارم":
                                    po4 = await bot.ask(message.chat.id , text="پنل چهارم تایید شد ✅\n\n💢 قیمت را حتما به عدد ارسال نمایید 💢")
                                    po4t = po4.text
                                    money_num_panel4.append(f"{po4t}")
                                    await bot.send_message(message.chat.id , text=f"قیمت تعیین شد ✅\n\n📲 شماره امریکا {po4t}💎")
                                else:
                                    await bot.send_message(message.chat.id , text="💢 عملیات لغو شد")
                                
            else:
                await bot.send_message(message.chat.id , text=f"💵 قیمت فعلی : {money_num[0]} 💎 \n\nهر 💎 معادل هزارتومان میباشد ‼️")
                poi = await bot.ask(message.chat.id , text="آیا میخواهید قیمت جدید تعیین کنید ❓\n\nyes/no")
                poit = poi.text
                if poit == "yes":
                    lk = await bot.ask(message.chat.id , text="🔰 قیمت را برای پنل های فروش خود تعیین نمایید .\n\n💢 توجه : شما میتوانید با ارسال پیام های << پنل اول >> و << پنل دوم >> و << پنل سوم >> و << پنل چهارم >> قیمت را برای هر پنل تعیین کنید 💢\n\nدرنظر داشته باشید باید قیمت را حتما عدد ارسال کنید ❕")
                    qlk = lk.text
                    if qlk is None :
                        await bot.send_message(message.chat.id , text="‼️ قیمتی تعیین نشد ‼️")
                    else:
                        qlkt = qlk
                        if qlkt == "پنل اول" :
                            qpo = await bot.ask(message.chat.id , text="پنل اول تایید شد ✅\n\n💢 قیمت را حتما به عدد ارسال نمایید 💢")
                            qpot = qpo.text
                            money_num.append(f"{qpot}")
                            await bot.send_message(message.chat.id , text=f"قیمت تعیین شد ✅\n\n📲 شماره امریکا {qpot}💎")
                        else:
                            if qlkt == "پنل دوم" :
                                qpo1 = await bot.ask(message.chat.id , text="پنل دوم تایید شد ✅\n\n💢 قیمت را حتما به عدد ارسال نمایید 💢")
                                qpo1t = qpo1.text
                                money_num_panel2.append(f"{qpo1t}")
                                await bot.send_message(message.chat.id , text=f"قیمت تعیین شد ✅\n\n📲 شماره امریکا {qpo1t}💎")
                            else:
                                if qlkt == "پنل سوم":
                                    qpo3 = await bot.ask(message.chat.id , text="پنل سوم تایید شد ✅\n\n💢 قیمت را حتما به عدد ارسال نمایید 💢")
                                    qpo3t = qpo3.text
                                    money_num_panel3.append(f"{qpo3t}")
                                    await bot.send_message(message.chat.id , text=f"قیمت تعیین شد ✅\n\n📲 شماره امریکا {qpo3t}💎")
                                else:
                                    if qlkt == "پنل چهارم":
                                        qpo4 = await bot.ask(message.chat.id , text="پنل چهارم تایید شد ✅\n\n💢 قیمت را حتما به عدد ارسال نمایید 💢")
                                        qpo4t = qpo4.text
                                        money_num_panel4.append(f"{qpo4t}")
                                        await bot.send_message(message.chat.id , text=f"قیمت تعیین شد ✅\n\n📲 شماره امریکا {qpo4t}💎")
                                    else:
                                        await bot.send_message(message.chat.id , text="💢 عملیات لغو شد")
                else:
                    await bot.send_message(message.chat.id , text="به مرحله قبل بازگشتید 🔙")
                    await Start(message , con , cur , get_balance , update_balance)



    if text == "بالانس توکنی📄":
        if user_id in list_admin :
            m = len(list_link)
            n = len(list_number)
            await bot.send_message(message.chat.id , text=f"🧾 تعداد موجودی توکن ها  << پنل اول >> : \n{m} عدد\n📲 تعداد موجودی شماره ها : \n{n} عدد")
            m1 = len(list_link_panel2)
            n1 = len(list_number_panel2)
            await bot.send_message(message.chat.id , text=f"🧾 تعداد موجودی توکن ها  << پنل دوم >> : \n{m1} عدد\n📲 تعداد موجودی شماره ها : \n{n1} عدد")
            m2 = len(list_link_panel3)
            n2 = len(list_number_panel3)
            await bot.send_message(message.chat.id , text=f"🧾 تعداد موجودی توکن ها  << پنل سوم >> : \n{m2} عدد\n📲 تعداد موجودی شماره ها : \n{n2} عدد")
            m3 = len(list_link_panel4)
            n3 = len(list_number_panel2)
            await bot.send_message(message.chat.id , text=f"🧾 تعداد موجودی توکن ها  << پنل چهارم >> : \n{m3} عدد\n📲 تعداد موجودی شماره ها : \n{n3} عدد")
    if text == "keyboard":
        if user_id in list_admin :
            p = await bot.ask(message.chat.id , text="💢 آیا میخواهید کیبورد را تغییر دهید ؟\nyes/no")
            pt = p.text
            if pt == "yes":
                q = await bot.ask(message.chat.id , text="🔰 گزینه دوم را تعیین نمایید :\n\n💢 توجه : سعی کنید گزینه ها را برای مثال به شکل زیر تعیین کنید ...\n🇺🇸آمریکا💎")
                qt = q.text
                keyboard_option[1].clear()
                keyboard_option[1].append(f"{qt}")
                w = await bot.ask(message.chat.id , text=f"گزینه دوم تایید شد ✅ ({qt})\n🔰 گزینه سوم را تعیین نمایید :\n\n💢 توجه : سعی کنید گزینه ها را برای مثال به شکل زیر تعیین کنید ...\n🇺🇸آمریکا💎")
                wt = w.text
                keyboard_option[2].clear()
                keyboard_option[2].append(f"{wt}")
                e = await bot.ask(message.chat.id , text=f"گزینه سوم تایید شد ✅ ({wt})\n🔰 گزینه چهارم را تعیین نمایید :\n\n💢 توجه : سعی کنید گزینه ها را برای مثال به شکل زیر تعیین کنید ...\n🇺🇸آمریکا💎")
                et = e.text
                keyboard_option[3].clear()
                keyboard_option[3].append(f"{et}")
                await bot.send_message(message.chat.id , text="عملیات با موفقیت انجام شد ✅\n\n💢 توجه : گزینه ها برای تست یکبار برای شما نمایش داده میشوند و نیاز به انتخاب انها نیست و فقط /start را بزنید 💢", reply_markup=ReplyKeyboardMarkup(keyboard=keyboard_option , resize_keyboard=True))
            else:
                await bot.send_message(message.chat.id , text="💢 عملیات لغو شد")
                await Start(message , con , cur , get_balance , update_balance)
    if text == "📞شماره مجازی":
        ppol =ReplyKeyboardMarkup(keyboard=keyboard_option , resize_keyboard=True)
        await bot.send_message(chat_id= message.chat.id , text="یکی از پنل ها را برای خرید انتخاب نمایید \n\nتوجه کنید!!:\nقبل از خرید حتما قسمت راهنما را مطالعه فرمایید", reply_markup=ppol)
        if text == "استعلام قیمت💰":
    if not bool(money_num) and not bool(money_num_panel2) and not bool(money_num_panel3) and not bool(money_num_panel4):
        await bot.send_message(message.chat.id , text="پنل فروش بسته است و قیمتی تعیین نشده است ❌\n\nدرحال تغییرات قیمت هستیم لطفا صبور باشید ❗️")
        await bot.send_message(chat_id = list_admin[0] , text="درخواست استعلام قیمت توسط کاربران ♻\n\nقیمتی برای شماره پنل ها پلتفرم تلگرام تعیین نشده است ‼️")
   else:
    time_now = datetime.now()
    message_text = f"""
    💠 نتیجه استعلام قیمت از پشتیبانی :\n\nپنل اول👑 :\n🌐 کشور : نامشخص\nپلتفرم : تلگرام 📱\nقیمت : {money_num[0] if money_num else 'ناموجود'}💎\n\n کشور : {keyboard_option[1] if len(keyboard_option) > 1 else 'نامشخص'}\nپلتفرم : تلگرام 📱\nقیمت : {money_num_panel2[0] if len(money_num_panel2) > 0 else 'ناموجود'}💎\n\nکشور : {keyboard_option[2] if len(keyboard_option) > 2 else 'نامشخص'}\nپلتفرم : تلگرام 📱\nقیمت : {money_num_panel3[0] if len(money_num_panel3) > 0 else 'ناموجود'}💎\n\nکشور : {keyboard_option[3] if len(keyboard_option) > 3 else 'نامشخص'}\nپلتفرم : تلگرام 📱\nقیمت : {money_num_panel4[0] if len(money_num_panel4) > 0 else 'ناموجود'}💎\n\nقیمت 💎 : هزارتومان\n🗓 اخرین تایم بروزرسانی قیمت در ...\n{time_now}
    """

    if text == "panel sell🗄":
        if user_id in list_admin :
            if sell_link and sell_num :
                await bot.send_message(message.chat.id , text=f"📑 توکن های فروش رفته : \n\n{sell_link}\n📲 شماره های فروش رفته : \n\n{sell_num}")
            else:
                await bot.send_message(message.chat.id , text="شماره و توکنی فروش نرفته است ⛔️")
    if text == "کد مجدد🔄":
        pwj = ReplyKeyboardMarkup(keyboard=[
            ["کد مجدد🔄","لغو سفارش❌"],
            ["تکمیل سفارش✅"]], resize_keyboard=True)
        cur.execute(f"SELECT number , phone FROM userbot WHERE userid = {user_id}")
        resualt = cur.fetchone()
        #print(resualt)
        if resualt :
            number = resualt[0]
            phone = resualt[1]
            if number and phone == 0:
                await bot.send_message(message.chat.id , text="شما درحال حاضر هیچ سفارشی در وضعیت باز ندارید ❌")
                #print("Number and phone and id = 0")
            else:
                for x in resualt :
                    if x == '0' :
                        await bot.send_message(message.chat.id , text="شما درحال حاضر هیچ سفارشی در وضعیت باز ندارید ❌")
                        #print("x = 0 : ",x)
                    else:
                        #print("x != 0 : ",x)
                        cur.execute(f"SELECT phon , tocken FROM userbot WHERE userid = {user_id}")
                        resualt_number = cur.fetchone()
                        if resualt_number != ('0', '0'):
                            phone1 = resualt_number[0]
                            tocken = resualt_number[1]
                            response = get(url=tocken)
                            rest = response.text
                            pattern = r'\d{5}'
                            code_c = re.findall(pattern , rest)
                            if bool(code_c) :
                                await bot.send_message(message.chat.id , text=f"📲 شماره : {phone1}\n🔑 کد ورود : {code_c}\n💢 سفارش شما بعد از 180 ثانیه ⏰ بصورت خودکار تکمیل میشود 💢", reply_markup=pwj)
                                await asyncio.sleep(180)
                                params = (0 , 0 , user_id)
                                cur.execute("UPDATE userbot SET phon = %s , tocken = %s WHERE userid = %s",params)
                                con.commit()
                            else:
                                await bot.send_message(message.chat.id , text=f"📲 شماره : {phone1}\n🔑 کد ورود : {code_c}\n💢 سفارش شما بعد از 180 ثانیه ⏰ بصورت خودکار تکمیل میشود 💢", reply_markup=pwj)
                                await asyncio.sleep(180)
                                params = (0 , 0 , user_id)
                                cur.execute("UPDATE userbot SET phon = %s , tocken = %s WHERE userid = %s",params)
                                con.commit()
                            #print("resualt_number : ",resualt_number)
                        else:
                            cur.execute(f"SELECT phone , token FROM userbot WHERE userid = {user_id}")
                            resualt_phone = cur.fetchone()
                            if resualt_phone != ('0','0') :
                                phone2 = resualt_phone[0]
                                token = resualt_phone[1]
                                response1 = get(url = token)
                                rew = response1.text
                                pattern1 = r'\d{5}'
                                code_c1 = re.findall(pattern1 , rew)
                                if bool(code_c1) :
                                    await bot.send_message(message.chat.id , text=f"📲 شماره : {phone2}\n🔑 کد ورود : {code_c1}\n💢 سفارش شما بعد از 180 ثانیه ⏰ بصورت خودکار تکمیل میشود 💢", reply_markup=pwj)
                                    await asyncio.sleep(180)
                                    params1 = (0 , 0 , user_id)
                                    cur.execute("UPDATE userbot SET phone = %s , token = %s WHERE userid = %s",params1)
                                    con.commit()
                                else:
                                    await bot.send_message(message.chat.id , text=f"📲 شماره : {phone2}\n🔑 کد ورود : {code_c1}\n💢 سفارش شما بعد از 180 ثانیه ⏰ بصورت خودکار تکمیل میشود 💢", reply_markup=pwj)
                                    await asyncio.sleep(180)
                                    params1 = (0 , 0 , user_id)
                                    cur.execute("UPDATE userbot SET phone = %s , token = %s WHERE userid = %s",params1)
                                    con.commit()
                                #print("resualt_phone : ",resualt_phone)
                                              
    if text == "لغو سفارش❌":
        cur.execute(f"SELECT number , phone FROM userbot WHERE userid = {user_id}")
        resualt = cur.fetchone()
        #print(resualt)
        if resualt :
            number = resualt[0]
            phone = resualt[1]
            if number and phone == 0:
                await bot.send_message(message.chat.id , text="شما درحال حاضر هیچ سفارشی در وضعیت باز ندارید❌\n\n/start")
                #print("Number and phone and id = 0")
                
            else:
                for x in resualt :
                    if x == '0' :
                        await bot.send_message(message.chat.id , text="شما درحال حاضر هیچ سفارشی در وضعیت باز ندارید❌\n\n/start")
                        #print("x = 0 : ",x)
                    else:
                        #print("x != 0 : ",x)
                        cur.execute(f"SELECT phon , tocken FROM userbot WHERE userid = {user_id}")
                        resualt_number = cur.fetchone()
                        if resualt_number != ('0', '0'):
                            phone1 = resualt_number[0]
                            tocken = resualt_number[1]
                            list_link.append(tocken)
                            list_number.append(phone1)
                            amount = money_num[0]
                            param = (0 , 0 , 0 , user_id)
                            cur.execute("UPDATE userbot SET number = %s, phon = %s , tocken = %s WHERE userid = %s",param)
                            con.commit()
                            await increase_balance(user_id, amount)
                            await bot.send_message(message.chat.id , text=f"💠 سفارش شما با موفقیت لغو شد و مبلغ کسر شده به حساب شما بازگشت خورد 🤑")
                            await Start(message , con , cur , get_balance , update_balance)
                            #print("resualt_number : ",resualt_number)
                        else:
                            cur.execute(f"SELECT phone , token FROM userbot WHERE userid = {user_id}")
                            resualt_phone = cur.fetchone()
                            if resualt_phone != ('0','0') :
                                phone2 = resualt_phone[0]
                                token = resualt_phone[1]
                                if money_num:
    amount = money_num[0]
else:
    amount = 0  # or any other appropriate default value

                                list_link.append(token)
                                list_number.append(phone2)
                                param1 = (0 , 0 , user_id)
                                cur.execute("UPDATE userbot SET phone = %s , token = %s WHERE userid = %s",param1)
                                con.commit()
                                await increase_balance(user_id, amount)
                                await bot.send_message(message.chat.id , text=f"💠 سفارش شما با موفقیت لغو شد و مبلغ کسر شده به حساب شما بازگشت خورد 🤑")
                                await Start(message , con , cur , get_balance , update_balance)
                                #print("resualt_phone : ",resualt_phone)

                
             
                     
    if text == "تکمیل سفارش✅":
        cur.execute(f"SELECT number , phone FROM userbot WHERE userid = {user_id}")
        resualt = cur.fetchone()
        #print(resualt)
        if resualt :
            number = resualt[0]
            phone = resualt[1]
            if number and phone == 0:
                await bot.send_message(message.chat.id , text="شما درحال حاضر هیچ سفارشی در وضعیت باز ندارید ❌\n\n/start")
                #print("Number and phone and id = 0")
            else:
                for x in resualt :
                    if x == '0' :
                        await bot.send_message(message.chat.id , text="شما درحال حاضر هیچ سفارشی در وضعیت باز ندارید ❌\n\n/start")
                        
                        #print("x = 0 : ",x)
                    else:
                        #print("x != 0 : ",x)
                        cur.execute(f"SELECT phon , tocken FROM userbot WHERE userid = {user_id}")
                        resualt_number = cur.fetchone()
                        if resualt_number != ('0', '0'):
                            phone1 = resualt_number[0]
                            tocken = resualt_number[1]
                            hidden = "*" * (len(phone1) -7)
                            last_four = phone1[-7:]
                            hide = hidden + last_four
                            paramsa = (0 , 0 , 0 , user_id)
                            cur.execute("UPDATE userbot SET number = %s , phon = %s , tocken = %s WHERE userid = %s",paramsa)
                            con.commit()
                            await bot.send_message( chat_id = "@Numberturbo_kharid", text=f"💠 خرید یک شماره از فروشگاه 🛍 با موفقیت انجام شد ✅ :\n📲 Number : {hide}\nقیمت بر اساس 💎", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📲خرید شماره مجازی ارزان😍" , url="https://t.me/Numberturbo_bot")]]))
                            await bot.send_message(message.chat.id , text=f"سفارش شما با موفقیت تکمیل شد 🎊")
                            await bot.send_message(message.chat.id , text=f"ممنون از اینکه ربات ما را برای خرید انتخاب کردید 😍")
                            await Start(message , con , cur , get_balance , update_balance)
                            #print("resualt_number : ",resualt_number)
                        else:
                            cur.execute(f"SELECT phone , token FROM userbot WHERE userid = {user_id}")
                            resualt_phone = cur.fetchone()
                            if resualt_phone != ('0','0') :
                                phone2 = resualt_phone[0]
                                token = resualt_phone[1]
                                hidden = "*" * (len(phone2) -7)
                                last_four = phone2[-7:]
                                hide = hidden + last_four
                                paramsa = (0 , 0 , user_id)
                                cur.execute("UPDATE userbot SET phone = %s , token = %s WHERE userid = %s",paramsa)
                                con.commit()
                                await bot.send_message(message.chat.id , text=f"سفارش شما با موفقیت تکمیل شد 🎊")
                                await bot.send_message(message.chat.id , text=f"ممنون از اینکه ربات ما را برای خرید انتخاب کردید 😍")
                                await bot.send_message( chat_id = "@Numberturbo_kharid", text=f"💠 خرید یک شماره از فروشگاه 🛍 با موفقیت انجام شد ✅ :\n📲 Number : {hide}\nقیمت بر اساس 💎", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📲خرید شماره مجازی ارزان😍" , url="https://t.me/Numberturbo_bot")]]))
                                await Start(message , con , cur , get_balance , update_balance)
                                #print("resualt_phone : ",resualt_phone) 
                                



        
    if text == "پنل اول👑":
        if money_num :
            if status_list :
                if status_list[0] == 1:
                    if not list_number:
                        await bot.send_message(chat_id=message.chat.id, text="🛑 موجودی شماره های این پنل صفر است !!\n\n🔰 لطفا از پنل دیگری استفاده نمایید")
                        await bot.send_message(chat_id=list_admin[0] , text="💢 بالانس پنل اول فروش (🛍 محصولات توکنی) صفر است ‼️\n\nهرچه سریعتر اقدام به شارژ این پنل و یا غیرفعال کردن پنل فروش کنید‼️\n\n💢 توجه این پنل توسط ربات بصورت خودکار غیرفعال شد 💢")                    
                    else:
                        cur.execute(f"SELECT number , phone , id FROM userbot WHERE userid = {user_id}")
                        resualt_4 = cur.fetchone()
                        if resualt_4 :
                            number = resualt_4[0]
                            phone = resualt_4[1]
                            id_idm = resualt_4[2]
                            if number or phone or id_idm == 0 :
                                price = money_num[0]
                                await check_and_purchase(message , user_id , price , cur , con)
                            else:
                                await bot.send_message(message.chat.id , text=f"💢 شما درحال حاضر یک سفارش در وضعیت باز دارید .\n\nبا استفاده از گزینه << 🪪اطلاعات اکانت >> میتوانید شماره سفارش خود را دیده و اقدامات لازم به ان را انجام دهید.")
                                await Start(message , con , cur , get_balance , update_balance)
                else:
                    await bot.send_message(chat_id=message.chat.id , text="⛔️ این پنل غیرفعال است")
            else:
                await bot.send_message(chat_id=message.chat.id , text="⛔️ این پنل غیرفعال است")
        else:
            await bot.send_message(chat_id=message.chat.id , text="⛔️ این پنل غیرفعال است")
    if [text] == keyboard_option[1]:
        if money_num_panel2 :
            if status_list_panel2 : 
                if status_list_panel2[0] == 1 :
                    if not list_number_panel2:
                        await bot.send_message(chat_id=message.chat.id, text="🛑 موجودی شماره های این پنل صفر است !!\n\n🔰 لطفا از پنل دیگری استفاده نمایید")
                        await bot.send_message(chat_id=list_admin[0] , text="💢 بالانس پنل دوم فروش (🛍 محصولات توکنی) صفر است ‼️\n\nهرچه سریعتر اقدام به شارژ این پنل و یا غیرفعال کردن پنل فروش کنید‼️\n\n💢 توجه این پنل توسط ربات بصورت خودکار غیرفعال شد 💢")                    
                    else:
                        cur.execute(f"SELECT number , phone , id FROM userbot WHERE userid = {user_id}")
                        resualt_4 = cur.fetchone()
                        if resualt_4 :
                            number = resualt_4[0]
                            phone = resualt_4[1]
                            id_idm = resualt_4[2]
                            if number or phone or id_idm == 0 :
                                price = money_num_panel2[0]
                                await check_and_purchase_panel2(message , user_id , price , cur , con)
                            else:
                                await bot.send_message(message.chat.id , text=f"💢 شما درحال حاضر یک سفارش در وضعیت باز دارید .\n\nبا استفاده از گزینه << 🪪اطلاعات اکانت >> میتوانید شماره سفارش خود را دیده و اقدامات لازم به ان را انجام دهید.")
                                await Start(message , con , cur , get_balance , update_balance)
                else:
                    await bot.send_message(chat_id=message.chat.id , text="⛔️ این پنل غیرفعال است")
            else:
                await bot.send_message(chat_id=message.chat.id , text="⛔️ این پنل غیرفعال است")
        else:
            await bot.send_message(chat_id=message.chat.id , text="⛔️ این پنل غیرفعال است")
    if [text] == keyboard_option[2]:
        if money_num_panel3 :
            if status_list_panel3 :
                if status_list_panel3[0] == 1:
                    if not list_number_panel3:
                        await bot.send_message(chat_id=message.chat.id, text="🛑 موجودی شماره های این پنل صفر است !!\n\n🔰 لطفا از پنل دیگری استفاده نمایید")
                        await bot.send_message(chat_id=list_admin[0] , text="💢 بالانس پنل سوم فروش (🛍 محصولات توکنی) صفر است ‼️\n\nهرچه سریعتر اقدام به شارژ این پنل و یا غیرفعال کردن پنل فروش کنید‼️\n\n💢 توجه این پنل توسط ربات بصورت خودکار غیرفعال شد 💢")                    
                    else:
                        cur.execute(f"SELECT number , phone , id FROM userbot WHERE userid = {user_id}")
                        resualt_4 = cur.fetchone()
                        if resualt_4 :
                            number = resualt_4[0]
                            phone = resualt_4[1]
                            id_idm = resualt_4[2]
                            if number or phone or id_idm == 0 :
                                price = money_num_panel3[0]
                                await check_and_purchase_panel3(message , user_id , price , cur , con)
                            else:
                                await bot.send_message(message.chat.id , text=f"💢 شما درحال حاضر یک سفارش در وضعیت باز دارید .\n\nبا استفاده از گزینه << 🪪اطلاعات اکانت >> میتوانید شماره سفارش خود را دیده و اقدامات لازم به ان را انجام دهید.")
                                await Start(message , con , cur , get_balance , update_balance)
                else:
                    await bot.send_message(chat_id=message.chat.id , text="⛔️ این پنل غیرفعال است")
            else:
                await bot.send_message(chat_id=message.chat.id , text="⛔️ این پنل غیرفعال است")
        else:
            await bot.send_message(chat_id=message.chat.id , text="⛔️ این پنل غیرفعال است")
    if [text] == keyboard_option[3]:
        if money_num_panel4 :
            if status_list_panel4 :
                if status_list_panel4[0] == 1 :
                    if not list_number_panel4:
                        await bot.send_message(chat_id=message.chat.id, text="🛑 موجودی شماره های این پنل صفر است !!\n\n🔰 لطفا از پنل دیگری استفاده نمایید")
                        await bot.send_message(chat_id=list_admin[0] , text="💢 بالانس پنل چهارم فروش (🛍 محصولات توکنی) صفر است ‼️\n\nهرچه سریعتر اقدام به شارژ این پنل و یا غیرفعال کردن پنل فروش کنید‼️\n\n💢 توجه این پنل توسط ربات بصورت خودکار غیرفعال شد 💢")                    
                    else:
                        cur.execute(f"SELECT number , phone , id FROM userbot WHERE userid = {user_id}")
                        resualt_4 = cur.fetchone()
                        if resualt_4 :
                            number = resualt_4[0]
                            phone = resualt_4[1]
                            id_idm = resualt_4[2]
                            if number or phone or id_idm == 0 :
                                price = money_num_panel4[0]
                                await check_and_purchase_panel4(message , user_id , price , cur , con)
                            else:
                                await bot.send_message(message.chat.id , text=f"💢 شما درحال حاضر یک سفارش در وضعیت باز دارید .\n\nبا استفاده از گزینه << 🪪اطلاعات اکانت >> میتوانید شماره سفارش خود را دیده و اقدامات لازم به ان را انجام دهید.")
                                await Start(message , con , cur , get_balance , update_balance)
                else:
                    await bot.send_message(chat_id=message.chat.id , text="⛔️ این پنل غیرفعال است")
            else:
                await bot.send_message(chat_id=message.chat.id , text="⛔️ این پنل غیرفعال است")
        else:
            await bot.send_message(chat_id=message.chat.id , text="⛔️ این پنل غیرفعال است")
    if text == "SET-Status-list📝":
        if user_id in list_admin :
            nm =await bot.ask(chat_id , text="🔰 وضعیت فروش را برای پنل های مختلف با ارسال پیام های \n<< پنل اول >>\n<< پنل دوم >>\n<< پنل سوم >>\n<< پنل چهارم >>\nتعیین کنید .")
            nmt = nm.text
            if nmt == "پنل اول":
                q = await bot.ask(message.chat.id , text="🔰 وضعیت پنل اول را تعیین نمایید \n💢 ارسال پیام های enable/false مجاز است 💢")
                qt = q.text
                if qt == "enable" :
                    status_list.clear()
                    status_list.append(1)
                    await bot.send_message(chat_id=message.chat.id , text=f"🔰 وضعیت پنل اول : {qt}\nباموفقیت تغییر کرد ✅")
                else:
                    status_list.clear()
                    status_list.append(0)
                    await bot.send_message(chat_id=message.chat.id , text=f"🔰 وضعیت پنل اول : {qt}\nباموفقیت تغییر کرد ✅")
            else:
                if nmt == "پنل دوم":
                    w = await bot.ask(message.chat.id , text="🔰 وضعیت پنل دوم را تعیین نمایید \n💢 ارسال پیام های enable/false مجاز است 💢")
                    wt = w.text 
                    if wt == "enable":
                        status_list_panel2.clear()
                        status_list_panel2.append(1)
                        await bot.send_message(chat_id=message.chat.id , text=f"🔰 وضعیت پنل دوم : {wt}\nباموفقیت تغییر کرد ✅")
                    else:
                        status_list_panel2.clear()
                        status_list_panel2.append(0)
                        await bot.send_message(chat_id=message.chat.id , text=f"🔰 وضعیت پنل دوم : {wt}\nباموفقیت تغییر کرد ✅")
                else:
                    if nmt == "پنل سوم":
                        e = await bot.ask(message.chat.id , text="🔰 وضعیت پنل سوم را تعیین نمایید \n💢 ارسال پیام های enable/false مجاز است 💢")
                        et = e.text
                        if et == "enable":
                            status_list_panel3.clear()
                            status_list_panel3.append(1)
                            await bot.send_message(chat_id=message.chat.id , text=f"🔰 وضعیت پنل سوم : {et}\nباموفقیت تغییر کرد ✅")
                        else:
                            status_list_panel3.clear()
                            status_list_panel3.append(0)
                            await bot.send_message(chat_id=message.chat.id , text=f"🔰 وضعیت پنل سوم : {et}\nباموفقیت تغییر کرد ✅")
                    else:
                        if nmt == "پنل چهارم":
                            r = await bot.ask(message.chat.id , text="🔰 وضعیت پنل چهارم را تعیین نمایید \n💢 ارسال پیام های enable/false مجاز است 💢")
                            rt = r.text
                            if rt == "enable":
                                status_list_panel4.clear()
                                status_list_panel4.append(1)
                                await bot.send_message(chat_id=message.chat.id , text=f"🔰 وضعیت پنل چهارم : {rt}\nباموفقیت تغییر کرد ✅")
                            else:
                                status_list_panel4.clear()
                                status_list_panel4.append(0)
                                await bot.send_message(chat_id=message.chat.id , text=f"🔰 وضعیت پنل چهارم : {rt}\nباموفقیت تغییر کرد ✅")
                        else:
                            await bot.send_message(message.chat.id , text="💢 عملیات لغو شد")
                            await Start(message , con , cur , get_balance , update_balance)
                            
    if text == "list🗃":
        if user_id in list_admin :

            if status_list and status_list_panel2 and status_list_panel3 and status_list_panel4 :
                if status_list[0] == 1 and status_list_panel2[0] == 1 and status_list_panel3[0] == 1 and status_list_panel4[0] == 1:
                    lkp = await bot.ask(chat_id , "میخواهید توکن جدید به لیست اضافه کنید ❓ \n💢 با ارسال پیام های \n<< پنل اول >>\n<< پنل دوم >>\n<< پنل سوم >>\n<< پنل چهارم >>\n پنل فروش مدنظر خود را تعیین کنید 💢")
                    lkpt = lkp.text
                    if lkpt == "پنل اول":
                        ppo = await bot.ask(chat_id , "توکن خود را ارسال کنید 📥")
                        ppot = ppo.text.splitlines()
                        #print(ppot)
                        if ppot is None :
                            await bot.send_message(chat_id , "📛 توکنی تایید نشد")
                        else:
                            if ppot in list_link:
                                await bot.send_message(chat_id , "⛔️ توکن ارسالی در لیست شما وجود دارد")
                            else:
                                list_link.append(ppot)
                                #print(list_link)
                                await bot.send_message(chat_id , "🗳 توکن شما باموفقیت داخل لیست ذخیره شد")
                                qqp = await bot.ask(chat_id=message.chat.id , text=f"📲 شماره مجازی توکن :\n{ppot}\nرا ارسال نمایید ❕")
                                qqpt = qqp.text.splitlines()
                                if qqpt is None :
                                    await bot.send_message(chat_id=message.chat.id , text="📛 شماره مجازی ارسال نشد")
                                else:
                                    if qqpt in list_number:
                                        await bot.send_message(chat_id=message.chat.id , text="⛔️ شماره ارسالی در لیست وجود دارد")
                                    else:
                                        list_number.append(qqpt)
                                        await bot.send_message(chat_id=message.chat.id , text=f"محصول جدید ...🧾\n\n📲 شماره مجازی : {qqpt}\n🗳 توکن شماره :\n{ppot}\n با موفقیت به پنل اول اضافه شد✅")
                    else:
                        if lkpt == "پنل دوم":
                            ppo = await bot.ask(chat_id , "توکن خود را ارسال کنید 📥")
                            ppot = ppo.text.splitlines()
                            #print(ppot)
                            if ppot is None :
                                await bot.send_message(chat_id , "📛 توکنی تایید نشد")
                            else:
                                if ppot in list_link_panel2:
                                    await bot.send_message(chat_id , "⛔️ توکن ارسالی در لیست شما وجود دارد")
                                else:
                                    list_link_panel2.append(ppot)
                                    #print(list_link)
                                    await bot.send_message(chat_id , "🗳 توکن شما باموفقیت داخل لیست ذخیره شد")
                                    qqp = await bot.ask(chat_id=message.chat.id , text=f"📲 شماره مجازی توکن :\n{ppot}\nرا ارسال نمایید ❕")
                                    qqpt = qqp.text.splitlines()
                                    if qqpt is None :
                                        await bot.send_message(chat_id=message.chat.id , text="📛 شماره مجازی ارسال نشد")
                                    else:
                                        if qqpt in list_number_panel2:
                                            await bot.send_message(chat_id=message.chat.id , text="⛔️ شماره ارسالی در لیست وجود دارد")
                                        else:
                                            list_number_panel2.append(qqpt)
                                            await bot.send_message(chat_id=message.chat.id , text=f"محصول جدید ...🧾\n\n📲 شماره مجازی : {qqpt}\n🗳 توکن شماره :\n{ppot}\n با موفقیت به پنل دوم اضافه شد✅")
                        else:
                            if lkpt == "پنل سوم":
                                ppo = await bot.ask(chat_id , "توکن خود را ارسال کنید 📥")
                                ppot = ppo.text.splitlines()
                                #print(ppot)
                                if ppot is None :
                                    await bot.send_message(chat_id , "📛 توکنی تایید نشد")
                                else:
                                    if ppot in list_link_panel3:
                                        await bot.send_message(chat_id , "⛔️ توکن ارسالی در لیست شما وجود دارد")
                                    else:
                                        list_link_panel3.append(ppot)
                                        #print(list_link)
                                        await bot.send_message(chat_id , "🗳 توکن شما باموفقیت داخل لیست ذخیره شد")
                                        qqp = await bot.ask(chat_id=message.chat.id , text=f"📲 شماره مجازی توکن :\n{ppot}\nرا ارسال نمایید ❕")
                                        qqpt = qqp.text.splitlines()
                                        if qqpt is None :
                                            await bot.send_message(chat_id=message.chat.id , text="📛 شماره مجازی ارسال نشد")
                                        else:
                                            if qqpt in list_number_panel3:
                                                await bot.send_message(chat_id=message.chat.id , text="⛔️ شماره ارسالی در لیست وجود دارد")
                                            else:
                                                list_number_panel3.append(qqpt)
                                                await bot.send_message(chat_id=message.chat.id , text=f"محصول جدید ...🧾\n\n📲 شماره مجازی : {qqpt}\n🗳 توکن شماره :\n{ppot}\n با موفقیت به پنل سوم اضافه شد✅")
                            else:
                                if lkpt == "پنل چهارم":
                                    ppo = await bot.ask(chat_id , "توکن خود را ارسال کنید 📥")
                                    ppot = ppo.text.splitlines()
                                    #print(ppot)
                                    if ppot is None :
                                        await bot.send_message(chat_id , "📛 توکنی تایید نشد")
                                    else:
                                        if ppot in list_link_panel4:
                                            await bot.send_message(chat_id , "⛔️ توکن ارسالی در لیست شما وجود دارد")
                                        else:
                                            list_link_panel4.append(ppot)
                                            #print(list_link)
                                            await bot.send_message(chat_id , "🗳 توکن شما باموفقیت داخل لیست ذخیره شد")
                                            qqp = await bot.ask(chat_id=message.chat.id , text=f"📲 شماره مجازی توکن :\n{ppot}\nرا ارسال نمایید ❕")
                                            qqpt = qqp.text.splitlines()
                                            if qqpt is None :
                                                await bot.send_message(chat_id=message.chat.id , text="📛 شماره مجازی ارسال نشد")
                                            else:
                                                if qqpt in list_number_panel4:
                                                    await bot.send_message(chat_id=message.chat.id , text="⛔️ شماره ارسالی در لیست وجود دارد")
                                                else:
                                                    list_number_panel4.append(qqpt)
                                                    await bot.send_message(chat_id=message.chat.id , text=f"محصول جدید ...🧾\n\n📲 شماره مجازی : {qqpt}\n🗳 توکن شماره :\n{ppot}\n با موفقیت به پنل چهارم اضافه شد✅")
                                else:
                                    await bot.send_message(message.chat.id , text="💢 عملیات لغو شد")
                                    await Start(message , con , cur , get_balance , update_balance)
                else:
                    await bot.send_message(chat_id=message.chat.id , text="پنل ها غیرفعال هستند ❗️\n💢 پنل ها را فعال کنید و بعد اقدام به شارژ پنل ها کنید") 

            else:
                await bot.send_message(chat_id=message.chat.id , text="پنل ها غیرفعال هستند ❗️\n💢 پنل ها را فعال کنید و بعد اقدام به شارژ پنل ها کنید")
    if text == "id-telegram":
        if user_id in list_admin :
            t = await bot.ask(chat_id , "👤 آیدی تلگرام کابر موردنظر خود را وارد نمایید")
            tm = t.text
            plo = await bot.get_users(f"{tm}")
            #print("id number user : ", plo.id)
        #=========================افزایش موجودی=====================#
            qw = await bot.ask(chat_id , "🔰 لطفا تعداد 💎 موردنظر خود را وارد نمایید\n\n📌 توجه : هر 💎 معادل هزارتومان میباشد")
            qwt = qw.text
            user_id_balance = plo.id
            #print(user_id_balance)
            amount = qwt
            await increase_balance(user_id_balance, amount)
            cur.execute(f"SELECT Balance FROM userbot WHERE userid = {user_id_balance}")
            resualt = cur.fetchone()
            if resualt :
                balance = resualt[0]
                if balance :
                    await bot.send_message(chat_id=message.chat.id , text=f"🧾 رسید افزایش موجودی :\n\nوضعیت : موفق ✅\n👤 آیدی عددی کاربر :{plo.id}\n🌟 آیدی تلگرامی کاربر : {tm}\nتعداد 💎 اضافه شده :{qwt}💎\n💰 موجودی فعلی کاربر : {balance}💎")
                else:
                    await bot.send_message(message.chat.id , text="⛔️ تراکنش انجام نشد ")
                    await Start(message , con , cur , get_balance , update_balance)

            
        
    if text == "id-number":
        if user_id in list_admin :
            n1 = await bot.ask(chat_id , "📖 آیدی عددی کابر موردنظر خود را وارد نمایید")
            user_id_b = n1.text
            qw1 = await bot.ask(chat_id=message.chat.id , text="🔰 لطفا تعداد 💎 موردنظر خود را وارد نمایید\n\n📌 توجه : هر 💎 معادل هزارتومان میباشد")
            qwt1 = qw1.text
            amount = qwt1
            await increase_balance(user_id_b, amount)
            cur.execute(f"SELECT Balance FROM userbot WHERE userid = {user_id_b}")
            resualt1 = cur.fetchone()
            if resualt1 :
                balance = resualt1[0]
                if balance :
                    await bot.send_message(chat_id=message.chat.id , text=f"🧾 رسید افزایش موجودی :\n\nوضعیت : موفق ✅\n👤 آیدی عددی کاربر :{user_id_b}\nتعداد 💎 اضافه شده :{qwt1}💎\n💰 موجودی فعلی کاربر : {balance}💎")
                else:
                    await bot.send_message(message.chat.id , text="⛔️ تراکنش انجام نشد ")
                    await Start(message , con , cur , get_balance , update_balance)     
    if text == "🛑error":
        if user_id in list_admin :
            if list_eror:
                await bot.send_message(message.chat.id , text=f"{list_eror}")
            else:
                await bot.send_message(message.chat.id , text="هیچ مقداری در لیست نیست")
                await Start(message , con , cur , get_balance , update_balance)
#-----------------------Start-----------------------#
async def Start(message , con , cur , get_balance , update_balance):
    text = message.text
    chat_id = message.chat.id
    user_id = message.from_user.id
    if user_id in list_admin:
        await bot.send_message(chat_id, text=f"سلام مدیر عزیز خوش اومدید👋")
        await Mange(message , con , cur , get_balance , update_balance)
    else:
        await bot.send_message(chat_id , text=f"سلام کاربر عزیز خیلی خیلی خوش اومدید👋")
        await user_account(message , con , cur , get_balance , update_balance)
        #print("user_id in Start : ",user_id)


#----------------------mange------------------------#
async def Mange(message , con , cur , get_balance , update_balance):
    text = message.text
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    cur.execute(f"SELECT userid FROM userbot WHERE userid = {user_id}")
    check = cur.fetchone()
    if check :
        userid = check[0]
        if userid == None :
            params = (user_id , 0 , 0 , 0 , 0 , 0 , 0)
            #print("user no exit in database")
            cur.execute("INSERT INTO userbot (userid , Balance , number , phon , tocken , phone , token) VALUES (%s,%s,%s,%s,%s,%s,%s)",params)
            con.commit()
            #print("New user added")

        else:
            await get_balance(user_id , con , cur , update_balance)
    else:
        params = (user_id , 0 , 0 , 0 , 0 , 0 , 0)
        #print("user no exit in database")
        cur.execute("INSERT INTO userbot (userid , Balance , number , phon , tocken , phone , token) VALUES (%s,%s,%s,%s,%s,%s,%s)",params)
        con.commit()
        #print("New user added")
        
    # await get_balance(user_id , con , cur , update_balance)
    mn = ReplyKeyboardMarkup(keyboard=[
        ["🗂تامین کننده ها"],
        ["کاهش موجودی🪫","🔋افزایش موجودی"],
        ["👨‍💻add admin","❌Delete admin"],
        ["👀show admin","show info📜"],
        ["📖کاربران","🧾پشتیبانی"]
    ], resize_keyboard=True)
    await bot.send_message(chat_id , text="chose button", reply_markup=mn)

#--------------------user--------------------------#
async def user_account(message , con , cur , get_balance , update_balance):
    text = message.text
    chat_id = message.chat.id
    user_id = message.from_user.id
    #print("user_id in user_account : ",user_id)
    cur.execute(f"SELECT userid FROM userbot WHERE userid = {user_id}")
    check = cur.fetchone()
    if check :
        userid = check[0]
        #print("userid in user_account : ",userid)
        if userid == None :
            params = (user_id , 0 , 0 , 0 , 0 , 0 , 0)
            #print("user no exit in database")
            cur.execute("INSERT INTO userbot (userid , Balance , number , phon , tocken , phone , token) VALUES (%s,%s,%s,%s,%s,%s,%s)",params)
            con.commit()
            #print("New user added")
        
        else:
            await get_balance(user_id , con , cur , update_balance)
    else:
        params = (user_id , 0 , 0 , 0 , 0 , 0 , 0)
        #print("user no exit in database")
        cur.execute("INSERT INTO userbot (userid , Balance , number , phon , tocken , phone , token) VALUES (%s,%s,%s,%s,%s,%s,%s)",params)
        con.commit()
        #print("New user added")

    # await get_balance(user_id , con , cur , update_balance)
    us = ReplyKeyboardMarkup(keyboard=[
        ["📞شماره مجازی"],
        ["🪪اطلاعات اکانت","💸افزایش موجودی"],
        ["🧑‍💻پشتیبانی","استعلام قیمت💰"]
    ],resize_keyboard=True)
    await bot.send_message(chat_id , f"🔰 {message.from_user.first_name}\nعزیز لطفا یکی از گزینه های زیر را انتخاب کنید", reply_markup=us)
#--------------------Add ALMAS with Admin--------------------------#
async def admony(message):
    chat_id = message.chat.id
    text = message.text
    user_id = message.from_user.id
    rk = ReplyKeyboardMarkup(keyboard=[
        ["id-telegram","id-number"],
        ["back🔙"]
    ], resize_keyboard=True)
    await bot.send_message(chat_id , "🔰 لطفا یکی از گزینه های زیر را انتخاب نمایید\nid-telegram : با استفاده از آیدی تلگرام مثل = @sijvjd\nid-number : با استفاده از آیدی عددی مثل = 83889222", reply_markup=rk)
#--------------------tamin--------------------------#
async def tamin(message):
    chat_id = message.chat.id 
    text = message.text
    user_id = message.from_user.id
    ke = ReplyKeyboardMarkup(keyboard=[
        ["تعیین قیمت💲","بالانس توکنی📄"],
        ["list🗃","SET-Status-list📝"],
        ["panel sell🗄","keyboard"],
        ["🛑error","back🔙"]
    ], resize_keyboard=True)
    await bot.send_message(chat_id , "chose button", reply_markup=ke)
   
#-----------------Panel 1 SEND PHONE---------------------------#
async def send_phone_panel1(message , price , list_link , list_number , head , user_id , generate_unique_number , sell_num , sell_link , list_eror):
    import requests
    import asyncio
    
    host = "localhost"
    database = "pnlturbo_botuser"
    user = "pnlturbo_root"
    password = "Root1botuser"
    con = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password)

    if con.is_connected():
        print("ok")
    else:
        print("Not ok")
        con.close()
    cur = con.cursor()
    pwj = ReplyKeyboardMarkup(keyboard=[
            ["کد مجدد🔄","لغو سفارش❌"],
            ["تکمیل سفارش✅"]], resize_keyboard=True)
    number_sell = ''.join(map(str , list_number[0]))
    # link = list_link[0]
    link = ''.join(map(str , list_link[0]))
    ttt = requests.get('https://www.google.com')
    print(ttt.status_code)
    response = requests.get(link)
    if response.status_code == 200 :
        pattern = r'\d{5}'
        code_number = response.text
        code = re.findall(pattern , code_number)
        if bool(code) :
            unique_number = generate_unique_number() 
            # text=f" شماره شما : {number_sell}\nقیمت : {price}\nکد : {code_number}\nشماره سفارش شما : {unique_number}\n\n توجه : 180 ثانیه فرصت دارید تا خرید خود را نهایی کنید !"
            await bot.send_message(chat_id=message.chat.id, text=f"🧾 رسید سفارش :\n🛍 محصولات :\n📲شماره مجازی تلگرام .. کشور امریکا 🇺🇸\n📱 شماره شما : {number_sell}\n💰قیمت : {price}💎\n🔐 کد ورود : {code_number}\n⚜ شماره سفارش : {unique_number}\n\n💢 توجه : 180 ثانیه ⏰ فرصت دارید تا سفارش خود را تکمیل نمایید", reply_markup=pwj)
            await bot.send_message(chat_id=message.chat.id , text="خرید با موفقیت انجام شد 😍")
            panel1_phone_data = True
            params = (unique_number,user_id)
            cur.execute("UPDATE userbot SET number =%s WHERE userid = %s",params)
            con.commit()
            params2 = (number_sell,link,user_id)
            cur.execute("UPDATE userbot SET phon = %s , tocken = %s WHERE userid = %s", params2)
            con.commit()
            sell_num.append(number_sell)
            sell_link.append(link)
            list_link.remove(list_link[0])
            list_number.remove(list_number[0])
            await asyncio.sleep(180)
            hidden = "*" * (len(number_sell) - 7)
            last_four = number_sell[-7:]
            hide = last_four + hidden 
            await bot.send_message( chat_id = "@Numberturbo_kharid", text=f"💠 سیگنال پنل اول 👑:\n\nخرید شماره با موفقیت انجام شد ✅\n📱 Number : {hide}\n💰 قیمت : {price}💎 ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📱خرید شماره مجازی ارزان😍" , url="https://t.me/Numberturbo_bot")]]))
            cur.execute(f"UPDATE userbot SET number = 0 , phon = 0 , tocken = 0 WHERE userid = {user_id}")
            con.commit()
            await bot.send_message(message.chat.id , text=f"💢 سفارش شما با شماره پیگیری :\n{unique_number}\nتکمیل شد 💢")
        else:
            para = (number_sell,link,user_id)
            cur.execute("UPDATE userbot SET phone = %s , token = %s WHERE userid = %s",para)
            con.commit()
            await bot.send_message(chat_id=message.chat.id, text=f"🧾 رسید سفارش :\n🛍 محصولات :\n📲شماره مجازی تلگرام .. کشور امریکا 🇺🇸\n📱 شماره شما : {number_sell}\n💰قیمت : {price}💎\n🔐 کد ورود : {code_number}", reply_markup=pwj)
            await bot.send_message(chat_id=message.chat.id , text="خرید با موفقیت انجام شد 😍")
            sell_num.append(number_sell)
            sell_link.append(link)
            list_link.remove(list_link[0])
            list_number.remove(list_number[0])
    else:
        list_eror.append(f"{link},{number_sell}")
        list_link.remove(list_link[0])
        list_number.remove(list_number[0])
        await increase_balance(user_id,price)
        await bot.send_message(message.chat.id , text=f"🔂 وضعیت چکر :\n💢 حذف شماره از پنل\nبازگشت موجودی به حساب شما ✅\n🔰 کاربر گرامی ربات دارای چکر اوتوماتیک است ( version = Beta)\n🔄 دوباره اقدام به خرید کنید")
        await Start(message , con , cur , get_balance , update_balance)
    #await pay_number(message , user_id , generate_unique_number)
    # #print(user_id)
    # param = (unique_number,user_id)
    # cur.execute("INSERT INTO userbot (userid , Balance , number) VALUES (userid , Balance , %s) WHERE userid = %s",param)
    # con.commit()
    # await bot.send_message(chat_id=message.chat.id, text=f"شماره شما : {number_sell}\nقیمت : {price}\nکد : {code_number}", reply_markup=pwj)
#-----------------Panel 2 SEND PHONE---------------------------#
async def send_phone_panel2(message , price , list_link_panel2 , list_number_panel2 , head , user_id , generate_unique_number , sell_num , sell_link , list_eror , keyboard_option):
    import requests
    import asyncio
    
    host = "localhost"
    database = "pnlturbo_botuser" 
    user = "pnlturbo_root" 
    password = "Root1botuser" 
    con = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password)

    if con.is_connected():
        print("ok")
    else:
        print("Not ok")
        con.close()
    cur = con.cursor()
    pwj = ReplyKeyboardMarkup(keyboard=[
            ["کد مجدد🔄","لغو سفارش❌"],
            ["تکمیل سفارش✅"]], resize_keyboard=True)
    number_sell = ''.join(map(str , list_number_panel2[0]))
    # link = list_link[0]
    link = ''.join(map(str , list_link_panel2[0]))
    ttt = requests.get('https://www.google.com')
    print(ttt.status_code)
    response = requests.get(link)
    if response.status_code == 200 :
        pattern = r'\d{5}'
        code_number = response.text
        code = re.findall(pattern , code_number)
        if bool(code) :
            unique_number = generate_unique_number() 
            # text=f" شماره شما : {number_sell}\nقیمت : {price}\nکد : {code_number}\nشماره سفارش شما : {unique_number}\n\n توجه : 180 ثانیه فرصت دارید تا خرید خود را نهایی کنید !"
            await bot.send_message(chat_id=message.chat.id, text=f"🧾 رسید سفارش :\n🛍 محصولات :\n📲شماره مجازی تلگرام .. کشور امریکا 🇺🇸\n📱 شماره شما : {number_sell}\n💰قیمت : {price}💎\n🔐 کد ورود : {code_number}\n⚜ شماره سفارش : {unique_number}\n\n💢 توجه : 180 ثانیه ⏰ فرصت دارید تا سفارش خود را تکمیل نمایید", reply_markup=pwj)
            await bot.send_message(chat_id=message.chat.id , text="خرید با موفقیت انجام شد 😍")
            params = (unique_number,user_id)
            cur.execute("UPDATE userbot SET number =%s WHERE userid = %s",params)
            con.commit()
            params2 = (number_sell,link,user_id)
            cur.execute("UPDATE userbot SET phon = %s , tocken = %s WHERE userid = %s", params2)
            con.commit()
            sell_num.append(number_sell)
            sell_link.append(link)
            list_link_panel2.remove(list_link_panel2[0])
            list_number_panel2.remove(list_number_panel2[0])
            await asyncio.sleep(180)
            hidden = "*" * (len(number_sell) - 7)
            last_four = number_sell[-7:]
            hide = last_four + hidden 
            await bot.send_message( chat_id = "@Numberturbo_kharid", text=f"خرید یک شماره {keyboard_option[1]} با موفقیت انجام شد ✅ :\n📱 Number : {hide}\n💰 قیمت : {price}💎 ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📱خرید شماره مجازی ارزان😍" , url="https://t.me/Numberturbo_bot")]]))
            cur.execute(f"UPDATE userbot SET number = 0 , phon = 0 , tocken = 0 WHERE userid = {user_id}")
            con.commit()
            await bot.send_message(message.chat.id , text=f"💢 سفارش شما با شماره پیگیری :\n{unique_number}\nتکمیل شد 💢")
        else:
            para = (number_sell,link,user_id)
            cur.execute("UPDATE userbot SET phone = %s , token = %s WHERE userid = %s",para)
            con.commit()
            await bot.send_message(chat_id=message.chat.id, text=f"🧾 رسید سفارش :\n🛍 محصولات :\n📲شماره مجازی تلگرام .. کشور امریکا 🇺🇸\n📱 شماره شما : {number_sell}\n💰قیمت : {price}💎\n🔐 کد ورود : {code_number}", reply_markup=pwj)
            await bot.send_message(chat_id=message.chat.id , text="خرید با موفقیت انجام شد 😍")
            sell_num.append(number_sell)
            sell_link.append(link)
            list_link_panel2.remove(list_link_panel2[0])
            list_number_panel2.remove(list_number_panel2[0])
    else:
        list_eror.append(f"{link},{number_sell}")
        list_link_panel2.remove(list_link_panel2[0])
        list_number_panel2.remove(list_number_panel2[0])
        await increase_balance(user_id,price)
        await bot.send_message(message.chat.id , text=f"🔂 وضعیت چکر :\n💢 حذف شماره از پنل\nبازگشت موجودی به حساب شما ✅\n🔰 کاربر گرامی ربات دارای چکر اوتوماتیک است ( version = Beta)\n🔄 دوباره اقدام به خرید کنید")
        await Start(message , con , cur , get_balance , update_balance)
    #await pay_number(message , user_id , generate_unique_number)
    # #print(user_id)
    # param = (unique_number,user_id)
    # cur.execute("INSERT INTO userbot (userid , Balance , number) VALUES (userid , Balance , %s) WHERE userid = %s",param)
    # con.commit()
    # await bot.send_message(chat_id=message.chat.id, text=f"شماره شما : {number_sell}\nقیمت : {price}\nکد : {code_number}", reply_markup=pwj)
#-----------------Panel 3 SEND PHONE---------------------------#
async def send_phone_panel3(message , price , list_link_panel3 , list_number_panel3 , head , user_id , generate_unique_number , sell_num , sell_link , list_eror , keyboard_option):
    import requests
    import asyncio
    
    host = "localhost"
    database = "pnlturbo_botuser" 
    user = "pnlturbo_root" 
    password = "Root1botuser" 
    con = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password)

    if con.is_connected():
        print("ok")
    else:
        print("Not ok")
        con.close()
    cur = con.cursor()
    pwj = ReplyKeyboardMarkup(keyboard=[
            ["کد مجدد🔄","لغو سفارش❌"],
            ["تکمیل سفارش✅"]], resize_keyboard=True)
    number_sell = ''.join(map(str , list_number_panel3[0]))
    # link = list_link[0]
    link = ''.join(map(str , list_link_panel3[0]))
    ttt = requests.get('https://www.google.com')
    print(ttt.status_code)
    response = requests.get(link)
    if response.status_code == 200 :
        pattern = r'\d{5}'
        code_number = response.text
        code = re.findall(pattern , code_number)
        if bool(code) :
            unique_number = generate_unique_number() 
            # text=f" شماره شما : {number_sell}\nقیمت : {price}\nکد : {code_number}\nشماره سفارش شما : {unique_number}\n\n توجه : 180 ثانیه فرصت دارید تا خرید خود را نهایی کنید !"
            await bot.send_message(chat_id=message.chat.id, text=f"🧾 رسید سفارش :\n🛍 محصولات :\n📲شماره مجازی تلگرام .. کشور امریکا 🇺🇸\n📱 شماره شما : {number_sell}\n💰قیمت : {price}💎\n🔐 کد ورود : {code_number}\n⚜ شماره سفارش : {unique_number}\n\n💢 توجه : 180 ثانیه ⏰ فرصت دارید تا سفارش خود را تکمیل نمایید", reply_markup=pwj)
            await bot.send_message(chat_id=message.chat.id , text="خرید با موفقیت انجام شد 😍")
            params = (unique_number,user_id)
            cur.execute("UPDATE userbot SET number =%s WHERE userid = %s",params)
            con.commit()
            params2 = (number_sell,link,user_id)
            cur.execute("UPDATE userbot SET phon = %s , tocken = %s WHERE userid = %s", params2)
            con.commit()
            sell_num.append(number_sell)
            sell_link.append(link)
            list_link_panel3.remove(list_link_panel3[0])
            list_number_panel3.remove(list_number_panel3[0])
            await asyncio.sleep(180)
            hidden = "*" * (len(number_sell) - 7)
            last_four = number_sell[-7:]
            hide = last_four + hidden 
            await bot.send_message( chat_id = "@Numberturbo_kharid", text=f"خرید یک شماره {keyboard_option[2]} با موفقیت انجام شد ✅ :\n📱 Number : {hide}\n💰 قیمت : {price}💎 ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📱خرید شماره مجازی ارزان😍" , url="https://t.me/Numberturbo_bot")]]))
            cur.execute(f"UPDATE userbot SET number = 0 , phon = 0 , tocken = 0 WHERE userid = {user_id}")
            con.commit()
            await bot.send_message(message.chat.id , text=f"💢 سفارش شما با شماره پیگیری :\n{unique_number}\nتکمیل شد 💢")
        else:
            para = (number_sell,link,user_id)
            cur.execute("UPDATE userbot SET phone = %s , token = %s WHERE userid = %s",para)
            con.commit()
            await bot.send_message(chat_id=message.chat.id, text=f"🧾 رسید سفارش :\n🛍 محصولات :\n📲شماره مجازی تلگرام .. کشور امریکا 🇺🇸\n📱 شماره شما : {number_sell}\n💰قیمت : {price}💎\n🔐 کد ورود : {code_number}", reply_markup=pwj)
            await bot.send_message(chat_id=message.chat.id , text="خرید با موفقیت انجام شد 😍")
            sell_num.append(number_sell)
            sell_link.append(link)
            list_link_panel3.remove(list_link_panel3[0])
            list_number_panel3.remove(list_number_panel3[0])
    else:
        list_eror.append(f"{link},{number_sell}")
        list_link_panel3.remove(list_link_panel3[0])
        list_number_panel3.remove(list_number_panel3[0])
        await increase_balance(user_id,price)
        await bot.send_message(message.chat.id , text=f"🔂 وضعیت چکر :\n💢 حذف شماره از پنل\nبازگشت موجودی به حساب شما ✅\n🔰 کاربر گرامی ربات دارای چکر اوتوماتیک است ( version = Beta)\n🔄 دوباره اقدام به خرید کنید")
        await Start(message , con , cur , get_balance , update_balance)
    #await pay_number(message , user_id , generate_unique_number)
    # #print(user_id)
    # param = (unique_number,user_id)
    # cur.execute("INSERT INTO userbot (userid , Balance , number) VALUES (userid , Balance , %s) WHERE userid = %s",param)
    # con.commit()
    # await bot.send_message(chat_id=message.chat.id, text=f"شماره شما : {number_sell}\nقیمت : {price}\nکد : {code_number}", reply_markup=pwj)
#-----------------Panel 4 SEND PHONE---------------------------#
async def send_phone_panel4(message , price , list_link_panel4 , list_number_panel4 , head , user_id , generate_unique_number , sell_num , sell_link , list_eror , keyboard_option):
    import requests
    import asyncio
    
    host = "localhost"
    database = "pnlturbo_botuser" 
    user = "pnlturbo_root" 
    password = "Root1botuser" 
    con = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password)

    if con.is_connected():
        print("ok")
    else:
        print("Not ok")
        con.close()
    cur = con.cursor()
    pwj = ReplyKeyboardMarkup(keyboard=[
            ["کد مجدد🔄","لغو سفارش❌"],
            ["تکمیل سفارش✅"]], resize_keyboard=True)
    number_sell = ''.join(map(str , list_number_panel4[0]))
    # link = list_link[0]
    link = ''.join(map(str , list_link_panel4[0]))
    ttt = requests.get('https://www.google.com')
    print(ttt.status_code)
    response = requests.get(link)
    if response.status_code == 200 :
        pattern = r'\d{5}'
        code_number = response.text
        code = re.findall(pattern , code_number)
        if bool(code) :
            unique_number = generate_unique_number() 
            # text=f" شماره شما : {number_sell}\nقیمت : {price}\nکد : {code_number}\nشماره سفارش شما : {unique_number}\n\n توجه : 180 ثانیه فرصت دارید تا خرید خود را نهایی کنید !"
            await bot.send_message(chat_id=message.chat.id, text=f"🧾 رسید سفارش :\n🛍 محصولات :\n📲شماره مجازی تلگرام .. کشور امریکا 🇺🇸\n📱 شماره شما : {number_sell}\n💰قیمت : {price}💎\n🔐 کد ورود : {code_number}\n⚜ شماره سفارش : {unique_number}\n\n💢 توجه : 180 ثانیه ⏰ فرصت دارید تا سفارش خود را تکمیل نمایید", reply_markup=pwj)
            await bot.send_message(chat_id=message.chat.id , text="خرید با موفقیت انجام شد 😍")
            params = (unique_number,user_id)
            cur.execute("UPDATE userbot SET number =%s WHERE userid = %s",params)
            con.commit()
            params2 = (number_sell,link,user_id)
            cur.execute("UPDATE userbot SET phon = %s , tocken = %s WHERE userid = %s", params2)
            con.commit()
            sell_num.append(number_sell)
            sell_link.append(link)
            list_link_panel4.remove(list_link_panel4[0])
            list_number_panel4.remove(list_number_panel4[0])
            await asyncio.sleep(180)
            hidden = "*" * (len(number_sell) - 7)
            last_four = number_sell[-7:]
            hide = last_four + hidden 
            await bot.send_message( chat_id = "@Numberturbo_kharid", text=f"خرید یک شماره {keyboard_option[3]} با موفقیت انجام شد ✅ :\n📱 Number : {hide}\n💰 قیمت : {price}💎 ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📱خرید شماره مجازی ارزان😍" , url="https://t.me/Numberturbo_bot")]]))
            cur.execute(f"UPDATE userbot SET number = 0 , phon = 0 , tocken = 0 WHERE userid = {user_id}")
            con.commit()
            await bot.send_message(message.chat.id , text=f"💢 سفارش شما با شماره پیگیری :\n{unique_number}\nتکمیل شد 💢")
        else:
            para = (number_sell,link,user_id)
            cur.execute("UPDATE userbot SET phone = %s , token = %s WHERE userid = %s",para)
            con.commit()
            await bot.send_message(chat_id=message.chat.id, text=f"🧾 رسید سفارش :\n🛍 محصولات :\n📲شماره مجازی تلگرام .. کشور امریکا 🇺🇸\n📱 شماره شما : {number_sell}\n💰قیمت : {price}💎\n🔐 کد ورود : {code_number}", reply_markup=pwj)
            await bot.send_message(chat_id=message.chat.id , text="خرید با موفقیت انجام شد 😍")
            sell_num.append(number_sell)
            sell_link.append(link)
            list_link_panel4.remove(list_link_panel4[0])
            list_number_panel4.remove(list_number_panel4[0])
    else:
        list_eror.append(f"{link},{number_sell}")
        list_link_panel4.remove(list_link_panel4[0])
        list_number_panel4.remove(list_number_panel4[0])
        await increase_balance(user_id,price)
        await bot.send_message(message.chat.id , text=f"🔂 وضعیت چکر :\n💢 حذف شماره از پنل\nبازگشت موجودی به حساب شما ✅\n🔰 کاربر گرامی ربات دارای چکر اوتوماتیک است ( version = Beta)\n🔄 دوباره اقدام به خرید کنید")
        await Start(message , con , cur , get_balance , update_balance)
    #await pay_number(message , user_id , generate_unique_number)
    # #print(user_id)
    # param = (unique_number,user_id)
    # cur.execute("INSERT INTO userbot (userid , Balance , number) VALUES (userid , Balance , %s) WHERE userid = %s",param)
    # con.commit()
    # await bot.send_message(chat_id=message.chat.id, text=f"شماره شما : {number_sell}\nقیمت : {price}\nکد : {code_number}", reply_markup=pwj)
#----------------NUMBER Payment---------------------------#
def generate_unique_number():
    number = random.sample(range(11), 10)
    number = ''.join(str(digit) for digit in number)
    return number

#unique_number = generate_unique_number()# هروقت این خط فعال باشه شماره سفارش میسازه 
##print(unique_number)
    #====================Check Balance=============#1
async def get_balance(user_id , con , cur , update_balance):
    userid = user_id
    params = (user_id , 0)
    #print("user_id in get_balance : ", user_id)
    cur.execute(f"SELECT Balance FROM userbot WHERE userid = {userid}")
    resualt = cur.fetchone()
    #print("resualt : ",resualt)
    if resualt :
        balance = resualt[0]
        #print(balance)
        if balance == 0:
            #print("balance : ", balance)
            await update_balance(user_id , 0)
        return balance
    else:
        cur.execute("INSERT INTO userbot (userid , Balance) VALUES (%s,%s)",params)
        con.commit()
        #print("new user added")
#====================Check Balance=============#

#====================Update Balance=============#2
async def update_balance(user_id, new_balance):
    #print("user_id in update : ",user_id)
    params = (new_balance , user_id)
    cur.execute("UPDATE userbot SET Balance = %s WHERE userid = %s",params)
    con.commit()
#====================Update Balance=============#   



#====================Payment Number=============#
async def pay_number(message , user_id , generate_unique_number):
    host = "localhost"
    database = "botuser" 
    user = "root" 
    password = "" 
    con = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password)

    if con.is_connected():
        print("ok2")
    else:
        print("Not ok")
        con.close()
    cur = con.cursor()
    userid = user_id 
    payment_number = generate_unique_number()
    params = (payment_number,userid)
    cur.execute("UPDATE userbot SET number =%s WHERE userid = %s",params)
    con.commit()
    
    




#====================Payment Number=============#1



#====================Increase  Balance=============#2 for payment-nextpay
async def increase_balance(user_id, amount):
    previous_balance = await get_balance(user_id , con , cur , update_balance)
    #print(previous_balance , " : balance pre")
    if previous_balance is None or previous_balance == 0:
        # در صورتی که موجودی قبلی صفر باشد
        await update_balance(user_id, amount)
    else:
        # در صورتی که موجودی قبلی مقدار غیرصفر داشته باشد
        new_balance = previous_balance + int(amount)
        await update_balance(user_id, new_balance)
#====================Increase  Balance=============#



async def perform_purchase(message, price):
    # اینجا می‌توانید عمل خرید را انجام دهید، مانند به‌روزرسانی پایگاه داده یا ارسال درخواست به سیستم پرداخت و ...
    # به عنوان مثال، اینجا یک پیام به کاربر برای تأیید خرید ارسال می‌شود
    await bot.send_message(chat_id=message.chat.id , text=f"خرید با مبلغ {price} ✅تومان تأیید شد.")
    
    
#====================Purchase  Balance=============#
async def check_and_purchase(message , user_id , price , cur , con):
    balance = await get_balance(user_id , con , cur , update_balance)
    if balance is None or balance == 0:
        # در صورتی که موجودی صفر باشد
        # callback_data ===> phonne.py (balance_user = 0)
        await bot.send_message(chat_id=message.chat.id, text="موجودی شما کافی نیست ⛔️\nمقدار بالانس شما 0💎 است ")
        return False
    elif balance >= int(price):
        # در صورتی که موجودی به اندازه قیمت محصول می‌رسد
        await bot.send_message(chat_id=message.chat.id , text=f"💠 امریکا {money_num[0]}💎 درحال خرید")
        new_balance = balance - int(price)
        price = int(price)
        await update_balance(user_id, new_balance)
        await perform_purchase(message, price)
        await send_phone_panel1(message , price , list_link , list_number , head , user_id , generate_unique_number , sell_num , sell_link , list_eror)
        
        return True
    else:
        # در صورتی که موجودی کافی نیست
        # callback_data ===> phone.py (balance_user is not enufe)
        await bot.send_message(chat_id=message.chat.id , text="موجودی شما کافی نیست ❌\n💢 بالانس خود را شارژ کنید بعد اقدام به خرید کنید")
        return False
#====================Purchase  Balance=============#


#====================Purchase2  Balance=============#
async def check_and_purchase_panel2(message , user_id , price , cur , con):
    balance = await get_balance(user_id , con , cur , update_balance)
    if balance is None or balance == 0:
        # در صورتی که موجودی صفر باشد
        # callback_data ===> phonne.py (balance_user = 0)
        await bot.send_message(chat_id=message.chat.id, text="موجودی شما کافی نیست ⛔️\nمقدار بالانس شما 0💎 است ")
        return False
    elif balance >= int(price):
        # در صورتی که موجودی به اندازه قیمت محصول می‌رسد
        await bot.send_message(chat_id=message.chat.id , text=f"💠 {keyboard_option[1]} {money_num_panel2[0]}💎 درحال خرید")
        new_balance = balance - int(price)
        price = int(price)
        await update_balance(user_id, new_balance)
        await perform_purchase(message, price)
        await send_phone_panel2(message , price , list_link_panel2 , list_number_panel2 , head , user_id , generate_unique_number , sell_num , sell_link , list_eror , keyboard_option)
        
        return True
    else:
        # در صورتی که موجودی کافی نیست
        # callback_data ===> phone.py (balance_user is not enufe)
        await bot.send_message(chat_id=message.chat.id , text="موجودی شما کافی نیست ❌\n💢 بالانس خود را شارژ کنید بعد اقدام به خرید کنید")
        return False
#====================Purchase2  Balance=============#


#====================Purchase3  Balance=============#
async def check_and_purchase_panel3(message , user_id , price , cur , con):
    balance = await get_balance(user_id , con , cur , update_balance)
    if balance is None or balance == 0:
        # در صورتی که موجودی صفر باشد
        # callback_data ===> phonne.py (balance_user = 0)
        await bot.send_message(chat_id=message.chat.id, text="موجودی شما کافی نیست ⛔️\nمقدار بالانس شما 0💎 است ")
        return False
    elif balance >= int(price):
        # در صورتی که موجودی به اندازه قیمت محصول می‌رسد
        await bot.send_message(chat_id=message.chat.id , text=f"💠 {keyboard_option[2]} {money_num_panel3[0]}💎 درحال خرید")
        new_balance = balance - int(price)
        price = int(price)
        await update_balance(user_id, new_balance)
        await perform_purchase(message, price)
        await send_phone_panel3(message , price , list_link_panel3 , list_number_panel3 , head , user_id , generate_unique_number , sell_num , sell_link , list_eror , keyboard_option)
        
        return True
    else:
        # در صورتی که موجودی کافی نیست
        # callback_data ===> phone.py (balance_user is not enufe)
        await bot.send_message(chat_id=message.chat.id , text="موجودی شما کافی نیست ❌\n💢 بالانس خود را شارژ کنید بعد اقدام به خرید کنید")
        return False
#====================Purchase3  Balance=============#

#====================Purchase4  Balance=============#
async def check_and_purchase_panel4(message , user_id , price , cur , con):
    balance = await get_balance(user_id , con , cur , update_balance)
    if balance is None or balance == 0:
        # در صورتی که موجودی صفر باشد
        # callback_data ===> phonne.py (balance_user = 0)
        await bot.send_message(chat_id=message.chat.id, text="موجودی شما کافی نیست ⛔️\nمقدار بالانس شما 0💎 است ")
        return False
    elif balance >= int(price):
        # در صورتی که موجودی به اندازه قیمت محصول می‌رسد
        await bot.send_message(chat_id=message.chat.id , text=f"💠 {keyboard_option[3]} {money_num_panel4[0]}💎 درحال خرید")
        new_balance = balance - int(price)
        price = int(price)
        await update_balance(user_id, new_balance)
        await perform_purchase(message, price)
        await send_phone_panel4(message , price , list_link_panel4 , list_number_panel4 , head , user_id , generate_unique_number , sell_num , sell_link , list_eror , keyboard_option)
        
        return True
    else:
        # در صورتی که موجودی کافی نیست
        # callback_data ===> phone.py (balance_user is not enufe)
        await bot.send_message(chat_id=message.chat.id , text="موجودی شما کافی نیست ❌\n💢 بالانس خود را شارژ کنید بعد اقدام به خرید کنید")
        return False
#====================Purchase4  Balance=============#

#====================Cansel  Balance=============#
async def cansel_balance(user_id , price , cur , con):
    past_balance = await get_balance(user_id , con , cur , update_balance)
    if past_balance is None or past_balance == 0 :
        # مقدار موجودی قبلی کاربر برابر با صفر است
        await update_balance(user_id , price)
        # موجودی کاربر را ابدیت میکنیم به مقدار قیمت شماره
    else:
        # مقدار موجودی کاربر برابر با 0 نیست
        new_balance = past_balance + int(price)
        # مقدار موجودی قبلی کاربر را با قیمت شماره جمع میکنیم
        await update_balance(user_id , new_balance)
        # مقدار الماس جدید را با موجودی کاربر ابدیت میکنیم
#====================Cansel  Balance=============#
            

#--------------------Support----------------------------#
async def support(message , list_ticket):
    user_id = message.from_user.id
    s = await bot.ask(message.chat.id , text=f"⚜ لطفا پیام خود را بفرستید تا پشتیبانان ما در اسرع وقت پاسخ شما را بدهند\n\n🔰 در غیراینصورت no را ارسال کنید تا عملیات لفو شود\n\nتوجه ‼️ :\nدرصورتی که میخواهید حساب خود را از طریق روش 💳 کارت به کارت شارژ کنید حتما در اول تیکت خود کارت به کارت را قید نمایید.")
    sa = s.text
    if sa == "no":
        await bot.send_message(message.chat.id , text="💢 عملیات لغو شد")
    else:
        user_id = message.from_user.id
        list_ticket.append(f"{user_id}")
        #print(user_id)
        #print(list_ticket)
        user_id1 = list_admin[0]
        await bot.send_message(chat_id=user_id1 , text=f"📮 تیکت پشتیبانی :\n👤 ایدی کاربر:{user_id}\n💬 متن پیام:\n{sa}")
        await bot.send_message(message.chat.id , text="تیکت شما ثبت شد و در اسرع وقت پشتیبانان ما پاسخ شما را میدهند 🙂")
#--------------------Support Admin----------------------------#
async def supportad(message , list_ticket):
    if not list_ticket :
        await bot.send_message(message.chat.id , text="تیکتی ارسال نشده است ❌")
    else:
        p = ReplyKeyboardMarkup(keyboard=[
            ["📝ارسال جواب","📄لیست کاربران"],
            ["پیام همگانی📣","back🔙"]
        ], resize_keyboard=True)
        await bot.send_message(message.chat.id , text="👤 پشتیبانی عزیز ...\nیکی از گزینه های زیر را انتخاب نمایید", reply_markup=p)
async def ans(message , list_ticket):
    q = await bot.ask(message.chat.id , text="🆔 ایدی عددی کاربر را ارسال کنید.")
    qt = q.text
    if qt in list_ticket :
        a = await bot.ask(message.chat.id , text="💬 پیام خود را ارسال نمایید")
        at = a.text
        await bot.send_message(chat_id=qt , text=at)
        await bot.send_message(message.chat.id , text=f"📧 تیکت با مشخصات ...\n\n🆔 ایدی عددی کاربر :\n{qt}\n💬 متن تیکت :\n{at}\n\nباموفقیت ارسال شد ✅")
        list_ticket.remove(qt)
        await bot.send_message(message.chat.id , text=f"📧 تیکت با مشخصات ...\n\n🆔 آیدی عددی : {qt}\n💢 باموفقیت از لیست تیکت حذف شد") 
    else:
        await bot.send_message(message.chat.id , text=f"📜 کاربری با مشخصات ...\n🆔 ایدی عددی :\n{qt}\nتیکتی ثبت نکرده است ❌")
#-----------------------Message For All-----------------------#
async def textall(message):
    host = "localhost"
    database = "pnlturbo_botuser" 
    user = "pnlturbo_root" 
    password = "Root1botuser" 
    con = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password)

    if con.is_connected():
        print("ok3")
    else:
        print("Not ok")
        con.close()
    cur = con.cursor()
    t = await bot.ask(message.chat.id , text="💬پیام خود را ارسال کنید")
    tt = t.text
    cur.execute("SELECT userid FROM userbot")
    resualt_users = cur.fetchall()
    if resualt_users :
        for x in resualt_users :
            for b in x :
                try:
                    await bot.send_message(chat_id = b , text=tt)
                except:
                    pass
    else:
        await bot.send_message(message.chat.id , text="کاربری وجود ندارد ❌")
            
                    
@bot.on_callback_query()
async def button_click(client , callback_query):
    button = callback_query.data
    chat_id = callback_query.message.chat.id
    if button == "50":
        # Create link bank transfer ===>peyment.py 
        await client.send_message(chat_id , text="💢 کاربر عزیز :\nروش شارژ حساب از طریق درگاه پرداخت در دست ساخت میباشد ‼️\n\n📌 لذا خواهشمندیم از طریق ارسال تیکت شارژ حساب با روش کارت به کارت به پشتیبانی اقدام به شارژ حساب خود کنید")
    if button == "100":
        # Create link bank transfer ===>peyment.py 
        await client.send_message(chat_id , text="💢 کاربر عزیز :\nروش شارژ حساب از طریق درگاه پرداخت در دست ساخت میباشد ‼️\n\n📌 لذا خواهشمندیم از طریق ارسال تیکت شارژ حساب با روش کارت به کارت به پشتیبانی اقدام به شارژ حساب خود کنید")
    if button == "150":
        await client.send_message(chat_id , text="💢 کاربر عزیز :\nروش شارژ حساب از طریق درگاه پرداخت در دست ساخت میباشد ‼️\n\n📌 لذا خواهشمندیم از طریق ارسال تیکت شارژ حساب با روش کارت به کارت به پشتیبانی اقدام به شارژ حساب خود کنید")
    if button == "200":
        await client.send_message(chat_id , text="💢 کاربر عزیز :\nروش شارژ حساب از طریق درگاه پرداخت در دست ساخت میباشد ‼️\n\n📌 لذا خواهشمندیم از طریق ارسال تیکت شارژ حساب با روش کارت به کارت به پشتیبانی اقدام به شارژ حساب خود کنید")


bot.run()
