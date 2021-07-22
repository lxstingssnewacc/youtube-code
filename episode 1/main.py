import keep_alive
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == '/thisisayoutubetutorial':
            await message.channel.send('You can edit this code')

keep_alive.keep_alive()
client = MyClient()
client.run('change to your bot token')
