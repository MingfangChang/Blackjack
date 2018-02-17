from hand import Hand
class DealerPlayer:
    def __str__(self):
        return "DealerPlayer"

    def make_bet(self, playerbank):
        pass

    def use_ace_hi(self, hand):
        "if user wants Ace to be 11 return true"
        if hand.has_ace()==True:
            if (hand.get_score() <= 21):
                return True  # 11
            else:
                return False  # 1
        else:
            return False


    def want_card(self, playerhand, playerbank, dealerhands, cards_dealt):

        if(dealerhands.get_score()<17):

            return True
        else:
            return False


