import os

from bababot.bababot import Bababot
from bababot.jokefetcher import JokeFetcher
from bababot.sussifier import Sussifier

def main():
    bababot = Bababot(JokeFetcher(), Sussifier())

    key = os.getenv('API_KEY')
    bababot.run(key)

if __name__ == '__main__':
    main()
