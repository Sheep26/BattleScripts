########################
## script_template.py ##
########################
# Welcome to BattleScripts! This is the file template for your script that you will submit as your BattleScript.

from script import Script, ACTIONS

'''
Variables available in Script class.

self.my_money = 0
self.their_money = 0
self.current_turn = 0
self.my_move_history = []
self.their_move_history = []
self.meaning_of_life = 42
'''

class ScriptTemplate(Script): # << Name your script here, before the parenthsis, no spaces, no special chars.
    # Initalize the script.
    def __init__(self):
        super().__init__() # This calls the script parent function.

    def steal_or_support(self): # This function dictates whether the script steals or supports.
        return ACTIONS.STEAL

script = ScriptTemplate() # << Put your scripts name here, before the parenthsis.