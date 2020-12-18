from discord import Client

from bababot.jokefetcher import JokeFetcher


class Bababot(Client):
    """Your Strict Asian dad bot"""

    joke_fetcher: JokeFetcher

    def __init__(self, joke_fetcher: JokeFetcher):
        super().__init__()
        self.joke_fetcher = joke_fetcher

    async def print_commands(self, message) -> None:
        await message.channel.send(
            '```Politely ask Baba the following:\n\n'

            '?info             Get to know your Baba\n'
            '!ping             Ping your Baba\n'
            '?joke             Listen to Baba joke\n'
            '?hot              Ask Baba to say "That\'s hot!"\n'
            '?commands         Show this list of commands\n'
            '?slap @username   Ask Baba to slap the person mentioned```'
        )

    async def on_ready(self) -> None:
        print(f"Logged on as {self.user}!")

    async def on_message(self, message) -> None:
        # print('{0.author}: {0.content}'.format(message))

        if (message.author == self.user):
            return

        if (message.content == '!ping'):
            await message.channel.send('pong!')

        if (message.content == '?joke'):
            await message.channel.send(await self.joke_fetcher.fetch())

        if ('fortnite' in message.content.lower()):
            await message.channel \
                    .send('Say Fortnite again son and your dog will be gone.')

        if (message.content == '?hot'):
            await message.channel.send('That\'s hot!')

        if (message.content == '?commands'):
            await self.print_commands(message)

        if (message.content == '?info'):
            await message.channel.send(
                'I am your Baba. '
                'You will listen to me. '
                'Disappoint me and I will disown you.\n\n'
                '*Send **!commands** in chat to see how to interact with '
                'your Baba*\n\n'
                'I was built by kdeleteme. You can find my brain at'
                ' https://gitlab.com/kdeleteme/bababot.'
            )

        if 'i\'m' in message.content.lower() \
           or 'im' in message.content.lower() \
           or 'i am' in message.content.lower():

            im_index = -1

            for index, word in enumerate(message.content.lower().split(' ')):
                if word == 'i\'m' or word == 'im' or word == 'am':
                    im_index = index
                    break

            if im_index >= 0:
                accepted_message = message.content.split(' ')

                noun_array = []
                for index, word in enumerate(message.content.split(' ')):
                    if index > im_index:
                        noun_array += [word.replace('.', '')]

                        if word[-1] == '.':
                            break

                noun = ' '.join(noun_array)
                await message.channel.send(f'Haro {noun}, I\'m Baba.')
                    
        if ('?slap' in message.content.lower()):
            await message.channel \
                         .send('I won\'t allow you children to resort to'
                               ' violence. You need to behave!')
