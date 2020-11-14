import random
import math

class Sussifier:
    """Determine if crewmates are suspicious or not."""

    MIN_ROLL = 0
    MAX_ROLL = 9

    def roll(self) -> bool:
        random.seed()
        return math.floor(random.randint(self.MIN_ROLL, self.MAX_ROLL)) \
        == self.MIN_ROLL

            
