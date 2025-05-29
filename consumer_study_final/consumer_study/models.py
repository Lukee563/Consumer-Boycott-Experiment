from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'consumer_study'
    PLAYERS_PER_GROUP = None  # We'll group manually
    NUM_ROUNDS = 3
    INITIAL_TOKENS = 20

class Subsession(BaseSubsession):
    def creating_session(subsession):
        import random
        players = subsession.get_players()
        
        # 10 total players: 4 control, 3 treatment 1, 3 treatment 2
        treatments = [0] * 4 + [1] * 3 + [2] * 3
        random.shuffle(treatments)

        for player, treatment in zip(players, treatments):
            player.treatment = treatment

        # group players by treatment
        treatment_groups = {0: [], 1: [], 2: []}
        for p in players:
            treatment_groups[p.treatment].append(p)

        # build group matrix
        group_matrix = [group for group in treatment_groups.values() if group]
        subsession.set_group_matrix(group_matrix)

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    treatment = models.IntegerField()  # 0 = Control, 1 = Boycott Only, 2 = Boycott + Peer Pressure
    tokens = models.IntegerField(initial=C.INITIAL_TOKENS)
    choice = models.StringField(
        choices=["Producer 1", "Producer 2"],
        widget=widgets.RadioSelect
    )