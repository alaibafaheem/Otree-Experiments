# Colour coding of text of file names tells you about updates to files:
# White: no change
# Green: new file but it was classed earlier
# Orange: These are not tracked by git
# Blue: changed files

from otree.api import *


doc = """
Implementation of contest games with selectable contest success function
"""


class C(BaseConstants):
    NAME_IN_URL = 'contest'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 3
    ENDOWMENT = Currency(10)
    COST_PER_TICKET = Currency(0.50)
    PRIZE = Currency(8)


class Subsession(BaseSubsession):
    is_paid = models.BooleanField()

    def setup_round(self):
        self.is_paid = True
        for group in self.get_groups():
            group.setup_round()


class Group(BaseGroup):
    prize = models.CurrencyField()

    def setup_round(self):
        self.group = C.PRIZE
        for player in self.get_players():
            player.setup_round()


class Player(BasePlayer):
    endowment = models.CurrencyField()
    cost_per_ticket = models.CurrencyField()
    tickets_purchased = models.IntegerField()

    def setup_round(self):
        self.endowment = C.ENDOWMENT
        self.cost_per_ticket = C.COST_PER_TICKET

# def creating_session(subsession):
#     subsession.setup_round()

# PAGES

class SetUpRound(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession):
        subsession.setup_round()


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
