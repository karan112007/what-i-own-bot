from telethon import TelegramClient, events, Button

api_id = 'YAHAN_APNA_API_ID_DALEIN'
api_hash = 'YAHAN_APNA_API_HASH_DALEIN'
bot_token = 'YAHAN_APNA_BOT_TOKEN_DALEIN'

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
