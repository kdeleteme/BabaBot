import discord
import re

from jokefetcher import JokeFetcher


class Bababot(discord.Client):
    """Your Asian dad bot"""

    joke_fetcher = JokeFetcher()

    async def print_commands(self, message):
        await message.channel.send(
            '```Your Baba understands the following commands:\n\n'

            '!info         Get to know your Baba\n'
            '!ping         Ping your Baba\n'
            '!joke         Listen to Baba\'s joke\n'
            '!hot          Ask Baba to say "That\'s hot!"\n'
            '!commands     Show this list of commands```'
        )

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('{0.author}: {0.content}'.format(message))

        if (message.author == self.user):
            return

        if (message.content == '!ping'):
            await message.channel.send('pong!')

        if (message.content == '!joke'):
            await message.channel.send(await self.joke_fetcher.start())

        if (re.search('fortnite', message.content.lower())):
            await message.channel \
                    .send('Say Fortnite again son and your dog will be gone.')

        if (message.content == '!hot'):
            await message.channel.send('That\'s hot!')

        if (message.content == '!commands'):
            await self.print_commands(message)

        if (message.content == '!info'):
            await message.channel.send(
                'I am your Baba. '
                'You will listen to me. '
                'Disappoint me and I will disown you.\n\n'
                '*Send **!commands** in chat to see how to interact with '
                'your Baba*'
            )
