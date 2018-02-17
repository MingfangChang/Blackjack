from hand import Hand
class ConservativePlayer:

    def make_bet(self, playerbank):

        return int(playerbank.get_balance()/5)



    def use_ace_hi(self, hand):
        if hand.has_ace()==True:
            if (hand.get_score() + 11 > 21):  # want 1
                return False

            elif (hand.get_score() + 1 == 21):  # want 1
                return False
            elif (hand.get_score() + 11 == 21):  # want 11
                return True
            else:  # want11
                return True
        else:
            return False


    def want_card(self, playerhand, playerbank, dealerhand, cards_dealt):    #always want card?
        if(playerhand.get_score()<17):
            return True
        else:
            return False

    def __str__(self):
        return "ConservativePlayer"




