from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *



app = ApplicationBuilder().token("6112491827:AAHXHfNQb-JqK55qgngzqlZwse_Ow1_NQ-g").build()

app.add_handler(CommandHandler("Hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))



print('server start')
app.run_polling()

# from progress.bar import Bar

# bar = Bar('Processing', max=20)
# for i in range(20):
#     # Do some work
#     bar.next()
# bar.finish()


# from isOdd import isOdd

# print(isOdd(1))
# print(isOdd(4))