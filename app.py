import os

from bababot import Bababot

def main():
    bababot = Bababot(joke_fetcher)
    key = os.getenv('API_KEY')
    bababot.run(key)

if __name__ == '__main__':
    main()
