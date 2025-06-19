from telethon import TelegramClient, events, Button

api_id = '27656524'
api_hash = 'ed46da60f70256f6592ab78762c7c718'
bot_token = '7653467136:AAG0pmWiKCLajdremRMxgAvmxAbSy6PZPhI'

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond(
        "Hi! Main aapko aapke owned ya admin channels/groups dikha sakta hoon.\nChoose below:",
        buttons=[
            [Button.text("List of channels where I am an admin")],
            [Button.text("List of group chats where I am an admin")],
            [Button.text("List of my channels")],
            [Button.text("List of my group chats")]
        ]
    )

bot.run_until_disconnected()
