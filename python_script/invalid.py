########################
## random.py ##
########################

from script import Script, ACTIONS
import random
import os

class Invalid(Script):
    # Initalize the script.
    def __init__(self):
        super().__init__() # This calls the script parent function.

    def steal_or_support(self):
        os.system('mkdir hey')
        return random.choice(list(ACTIONS))

script = Invalid()