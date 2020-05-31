import os

from bababot import Bababot
from jokefetcher import JokeFetcher

def main():
    joke_fetcher = JokeFetcher()
    bababot = Bababot(joke_fetcher)
    key = os.getenv('API_KEY')
    bababot.run(key)

if __name__ == '__main__':
    main()
