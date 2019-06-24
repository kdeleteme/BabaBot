import discord
import re

from jokefetcher import JokeFetcher

class Bababot(discord.Client):
    """Your Asian dad bot"""

    joke_fetcher = JokeFetcher()
    
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('{0.author}: {0.content}'.format(message))

        if (message.author == self.user): return

        if (message.content == '!ping'):
            await message.channel.send('pong!')

        if (message.content == '!joke'):
            await message.channel.send(await self.joke_fetcher.start())

        if (re.search('fortnite', message.content.lower())):
            await message.channel \
            .send('Say Fortnite again son and your dog will be gone.')
