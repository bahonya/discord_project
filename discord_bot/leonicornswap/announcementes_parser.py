from telethon import TelegramClient, events

api_id = 242...
api_hash = '8a06ca620417c9964a058e0dc...'
bot_token = '1474729480:AAEhUPmVX_m...'
channelId = '-36744...'

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

client.start()

@client.on(events.NewMessage(channelId))
async def main(event):
     me = client.get_me()
     print(me.stringify())
     print(event.stringify())
        

client.run_until_disconnected()