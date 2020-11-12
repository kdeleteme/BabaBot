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
