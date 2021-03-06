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


from discord.ext.commands import Bot, Cog, command

class CommandCog(Cog, name = 'Commands'):
    """List of available commands BabaBot understands."""

    def __init__(self, bot: Bot):
        self.bot = bot

    @command(name = 'ping',
             brief = 'Ping Baba.',
             description = 'Ping Baba. '
             'Use this command to play ping pong if that\'s your thing.')
    async def ping(self, ctx):
        await ctx.send('pong!')

    @command(name = 'joke',
             aliases = ['jk'],
             brief = 'Listen to Baba joke.',
             description = 'Listen to Baba tell a dad joke. Lame.')
    async def joke(self, ctx):
        await ctx.send(await self.bot.joke_fetcher.fetch())

    @command(name = 'hot',
             brief = 'Ask Baba to say "That\'s hot!".',
             description = 'Ask Baba to say "That\'s hot!". '
             'It seems Baba is a boomer who\'s a fan of Will Smith.')
    async def hot(self, ctx):
        await ctx.send('That\'s hot!')

    @command(name = 'info',
             aliases = ['i'],
             brief = 'Get to know Baba.',
             description = 'Get to know Baba. '
             'See information on Baba and his creator.')
    async def info(self, ctx):
        await ctx.send(
            'I am your Baba. You will listen to me. '
            'Disappoint me and I will disown you.\n\n'
            '*Send **?help** in chat to see how to interact with me.*\n\n'
            'I was built by kdeleteme. You can find my brain at'
            ' https://gitlab.com/kdeleteme/bababot.\n\n'
            'Donate to support my development at '
            'https://liberapay.com/kdeleteme/donate.'
        )
            
    @command(name = 'slap',
             brief = 'Ask Baba to slap someone.',
             usage = '@username',
             description = 'Ask Baba to slap someone. Be careful. '
             'Baba hates violence.')
    async def slap(self, ctx):
        await ctx.send('I won\'t allow you children to resort to violence. You need to behave!')

def setup(bot):
    bot.add_cog(CommandCog(bot))
