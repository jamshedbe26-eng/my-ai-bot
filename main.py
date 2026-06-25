import telebot
import requests

BOT_TOKEN = "8821350713:AAGnjwroBtmOJJ1j8kn62zmZuoa0i9DP4_U"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Салом! Мен сунъий интеллектли ёрдамчиман. Менга исталган саволингизни беришингиз мумкин, калитлар шарт эмас!")

@bot.message_handler(func=lambda message: True)
def handle_ai_chat(message):
    bot.send_chat_action(message.chat.id, 'typing')
    url = "https://cf-workers.com"
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": message.text}]
    }
    try:
        response = requests.post(url, json=payload, timeout=15)
        response_data = response.json()
        ai_response = response_data['choices']['message']['content']
        bot.reply_to(message, ai_response)
    except Exception as e:
        print(f"Хатолик: {e}")
        bot.reply_to(message, "Ҳозирча жавоб бера олмайман. Илтимос, кейинроқ уриниб кўринг.")

print("Бот ишга тушди...")
bot.infinity_polling()
