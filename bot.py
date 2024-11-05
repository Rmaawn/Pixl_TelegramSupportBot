from telegram import Update , InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext import  Application, Updater , ContextTypes , ApplicationBuilder , CommandHandler , MessageHandler , filters , CallbackQueryHandler



se = 0
re = 0
B = []

#start function
async def start (update:Update , context:ContextTypes.DEFAULT_TYPE):
    contact_key = [[InlineKeyboardButton('ارتباط با ما📞' , callback_data='1')]]
    contact_key2 = InlineKeyboardMarkup(contact_key)
    if update.message.chat.id != 879550183:
        await context.bot.send_message(chat_id = update.message.chat.id , text = 'سلام {}  به ربات پشتیبانی پیکسل وب خوش اومدی'.format(update.message.from_user.first_name) , reply_markup=contact_key2)
    else :
       await context.bot.send_message(chat_id = 879550183 ,text = 'سلام ، شما ادمین هستید.' )



async def send (update:Update , context:ContextTypes.DEFAULT_TYPE):
    global se , re , sender
    key = [[InlineKeyboardButton('پاسخ' , callback_data='2')],[InlineKeyboardButton('بلاک کردن ❌' , callback_data='3'),InlineKeyboardButton('آنبلاک کردن ✅' , callback_data='4')]]
    key_2 = InlineKeyboardMarkup(key)
    if se != 0 :
        if update.message.chat_id not in B :
            await context.bot.send_message(chat_id = 879550183 , text= update.message.text , reply_markup= key_2)
            await context.bot.send_message(chat_id = update.message.chat.id , text='پیام شما ارسال گردید.')
            await context.bot.send_message(chat_id = 879550183, text= 'این پیام از طرف https://t.me/{} میباشد.'.format(update.message.from_user.username))
            sender = update.message.chat_id
            se = 0
        else:
            await context.bot.send_message(chat_id = update.message.chat_id , text='شما بلاک شده اید.')

    if re != 0 :
        await context.bot.send_message(chat_id = sender , text='پاسخ ادمین به شما : \n {}'.format(update.message.text))
        await context.bot.send_message(chat_id = 879550183 , text='پاسختان ارسال شد.')
        re = 0

async def contact_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global se, re
    query = update.callback_query
    if query.data == '1':
        se = 1
        await context.bot.send_message(chat_id=query.message.chat.id, text='پیام خود را وارد نمایید.')
    if query.data == '2':
        await context.bot.send_message(chat_id=879550183, text='پاسخ خود را وارد نمایید.')
        re = 1
    if query.data == '3':
        B.append(sender)
        await context.bot.send_message(chat_id = 879550183 , text='کاربر مورد نظظر با چت ایدی {} بلاک شد'.format(sender))
    if query.data == '4':
        if sender in B :
            B.remove(sender)
            await context.bot.send_message(chat_id = 879550183 , text= 'کاربر مورد نظر با چت آیدی {} آنبلاک شد'.format(sender))
        else :
            await context.bot.send_message(chat_id = 879550183 , text= 'کاربر مورد نظر بلاک نیست')

#info function
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button_1 = [[InlineKeyboardButton('وبسایت پیکسل وب' , callback_data='5' , url='https://pixlweb.ir')] , [InlineKeyboardButton('ادمین بات' , callback_data='6' , url='https://t.me/pixl_web')]]
    button_2 = InlineKeyboardMarkup(button_1)
    await context.bot.send_message(chat_id = update.message.chat_id , text= 'برای ارتباط مستقیم با ادمین و یا مشاهده وبسایت انتخاب کنید'  , reply_markup = button_2)







if __name__ == "__main__":
    application = ApplicationBuilder().token("7026571031:AAFtePg_wybVuV4ieIvudHovWcFecaEGtFo").build()

    start_handler = CommandHandler('start',start)
    application.add_handler(start_handler)

    info_handler = CommandHandler('info',info)
    application.add_handler(info_handler)

    msg = MessageHandler(filters.TEXT , send)
    application.add_handler(msg)

    callback = CallbackQueryHandler(contact_buttons)
    application.add_handler(callback)

    application.run_polling()
