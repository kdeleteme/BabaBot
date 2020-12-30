# Copyright (C) 2020  Kent Delante <kdeleteme@tutanota.com>

# This file is part of BabaBot

# BabaBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# BabaBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with BabaBot.  If not, see <https://www.gnu.org/licenses/>.


from discord import Intents, Member
from discord.ext import commands
from discord.ext.commands import Bot

from bababot.jokefetcher import JokeFetcher


class Bababot(Bot):
    """Your Strict Asian dad bot"""

    joke_fetcher: JokeFetcher

    def __init__(self, joke_fetcher: JokeFetcher, intents: Intents):
        super().__init__(intents = intents, command_prefix='?')
        self.joke_fetcher = joke_fetcher

    def setup(self):
        self.load_extension('bababot.cogs.CommandCog')

    async def on_member_join(self, member: Member):
        channel = member.guild.system_channel

        if channel is not None:
            await channel.send(f"Welcome to the family, {member.mention}! "
                               "Don't disappoint me and you will be fine.")

    async def on_ready(self):
        print(f"Logged on as {self.user}!")
        self.setup()

    async def on_message(self, message):
        if (message.author.bot):
            return

        await self.process_commands(message)
        
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

        if ('fortnite' in message.content.lower()):
            await message.channel.send('Say Fortnite again son and your dog will be gone.')
