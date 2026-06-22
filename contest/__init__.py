# Colour coding of text of file names tells you about updates to files:
# White: no change
# Green: new file but it was classed earlier
# Orange: These are not tracked by git

from otree.api import *


doc = """
Implementation of contest games with selectable contest success function
"""


class C(BaseConstants):
    NAME_IN_URL = 'contest'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES

class SetUpRound(WaitPage):
    pass

class Intro(Page):
    pass

class Decision(Page):
    pass

class Outcome(Page):
    pass

class WaitForDecisions(WaitPage):
    pass

class EndBlock(Page):
    pass

# In python, suggested to put one item on each line if there's a list
page_sequence = [
    SetUpRound,
    Intro,
    Decision,
    WaitForDecisions,
    Outcome,
    EndBlock
]
