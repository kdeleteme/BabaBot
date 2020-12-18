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
