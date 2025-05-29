from otree.api import *
from .models import C, Subsession, Group, Player

class GroupWait(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'creating_session'

class Instructions(Page):
    def vars_for_template(player):
        if player.treatment == 1:
            message = "There is a boycott on Producer 1 due to unethical practices."
        elif player.treatment == 2:
            message = "There is a boycott on Producer 1 due to unethical practices.\n3 of your 4 group members said they would boycott Producer One."
        else:
            message = ""
        return dict(message=message)

class Purchase(Page):
    form_model = 'player'
    form_fields = ['choice']

    def vars_for_template(player):
        return dict(tokens=player.tokens)

    def before_next_page(player, timeout_happened):
        player.tokens -= 1  # Assuming 1 token per purchase

class Results(Page):
    def vars_for_template(player):
        return dict(choice=player.choice, tokens=player.tokens)

page_sequence = [GroupWait, Instructions, Purchase, Results]
