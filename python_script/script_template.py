########################
## script_template.py ##
########################
# Welcome to BattleScripts! This is the file template for your script that you will submit as your BattleScript.

from script import Script, ACTIONS

class ScriptTemplate(Script):
    # Initalize the script.
    def __init__(self):
        super().__init__() # This calls the script parent function.

    def steal_or_support(self):
        return ACTIONS['STEAL']

script = ScriptTemplate()