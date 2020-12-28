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


import json
import random

from urllib import request

class JokeFetcher():
      """Fetch dadjokes from reddit"""

      URL = 'https://icanhazdadjoke.com'

      async def fetch(self) -> str:
            req =  request.Request(self.URL)
            req.add_header('User-Agent', 'Bababot (https://gitlab.com/kdeleteme/bababot)')
            req.add_header('Accept', 'text/plain')
            
            with request.urlopen(req) as url:
                  return url.read().decode('utf-8')
