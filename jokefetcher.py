import json
import random

from urllib import request

class JokeFetcher():
      """Fetch dadjokes from reddit"""

      URL = 'https://www.reddit.com/r/dadjokes/.json'

      async def fetch(self) -> str:
            
            req = request.Request(self.URL, headers = {
                  'User-Agent' : 'Bababot'
            })
            
            with request.urlopen(req) as url:
                  data = json.loads(url.read().decode())
                  jokes = data['data']['children']
                  roll = random.randint(0, len(jokes) - 1)
                  return '**{0} {1}**\n\n*u/{2}*'.format(
                        jokes[roll]['data']['title'],
                        jokes[roll]['data']['selftext'],
                        jokes[roll]['data']['author']
                  )
