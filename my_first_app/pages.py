from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


#class MyPage(Page):
#    pass


#class ResultsWaitPage(WaitPage):
#
#    def after_all_players_arrive(self):
#        pass


class Intro(Page):
    def before_next_page(self):
        toguess = random.randint(Constants.minguess,
                                 Constants.maxguess)
        self.player.toguess = toguess
    pass


class Decision(Page):
    form_model = 'player'
    form_fields = ['guess']
    def before_next_page(self):
        diff = abs(self.player.guess - self.player.toguess)
        self.player.payoff = Constants.endowment - diff
    pass


class Results(Page):
    def vars_for_template(self):
        return {
            'diff': abs(self.player.guess - self.player.toguess)
        }
    pass


page_sequence = [
    Intro,
    Decision,
    Results
]
