import random

class RandomPlayer:
    def __str__(self):
        return 'RandomPlayer'

    def make_bet(self, playerbank):
        return random.randint(0, playerbank.get_balance())


    def use_ace_hi(self, hand):
        if hand.has_ace():
            return random.choice([True, False])
        else:
            return False



    def want_card(self, playerhand, playerbank, dealerhard, cards_dealt):
        return random.choice([True, False])



