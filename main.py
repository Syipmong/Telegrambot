# Importing Required Libraries, Imported os Module For Security 
import os, telebot

# Getting Bot Token From Secrets
BOT_TOKEN = os.environ.get('BOT_TOKEN')

# Creating Telebot Object
bot = telebot.TeleBot(BOT_TOKEN)

# Whenever Starting Bot
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
  
  # Inline Button
  markup = telebot.types.InlineKeyboardMarkup()
  markup.add(telebot.types.InlineKeyboardButton("Use Template", url="https://replit.com/@krbishnoi46/Python-Telegram-Bot"))

  # Reply Keyboard Button
  # markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
  # markup.add(telebot.types.KeyboardButton("Reply Keyboard Button"))
  
  markdown = f"""Hey *{message.chat.first_name}* Welcome To *KR's Python Telegram Bot Template*.\n\nYou Can Use This Template By Visiting Our Template Page From This Below Button"""
  
  bot.reply_to(message, markdown, parse_mode="Markdown", reply_markup=markup)
  print(f"Welcome Message Sent To {message.chat.first_name}\n")

# Handle Documents
@bot.message_handler(func=lambda m: True, content_types=['document'])
def handle_docs_photo(message):
  bot.reply_to(message, f"Sorry {message.chat.first_name}, Documents Not Supported At This Time")
  print(f"Message Replied To {message.chat.first_name}\n")

# Reply To All Messages
@bot.message_handler(func=lambda msg: True)
def all(message):
  bot.reply_to(message, f"Sorry {message.chat.first_name}, This Bot Is In Development Mode")
  print(f"Message Replied To {message.chat.first_name}\n")

print("Bot Started And Waiting For New Messages\n")
  
# Waiting For New Messages
bot.infinity_polling()