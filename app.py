import os

from bababot.bababot import Bababot
from bababot.jokefetcher import JokeFetcher


def main():
    bababot = Bababot(JokeFetcher())

    key = os.getenv('API_KEY')
    bababot.run(key)

if __name__ == '__main__':
    main()
