import os

from bababot import Bababot

if __name__ == '__main__':
    key = os.environ['API_KEY']
    bababot = Bababot()
    bababot.run(key)
