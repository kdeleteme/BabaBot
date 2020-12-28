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


import os

from discord import Intents

from bababot.bababot import Bababot
from bababot.jokefetcher import JokeFetcher

def main():
    intents = Intents.default()
    intents.members = True
    bababot = Bababot(JokeFetcher(), intents)

    key = os.getenv('API_KEY')
    bababot.run(key)

if __name__ == '__main__':
    main()
