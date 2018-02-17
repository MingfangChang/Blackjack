from french_deck import FrenchDeck
from hand import Hand
from player_bank import PlayerBank
from dealerplayer import DealerPlayer
import random


class Dealer:
    def __init__(self, _deck):
        self._deck=FrenchDeck()       #french deck
        self._dealer=DealerPlayer()
        self._dealer_hand=Hand()
        self._players={}
        self._cards_dealt=[]

    def add_player(self, name, player, playerbank):
        if name in self._players:
            raise RuntimeError("Handle is already a key.")
        else:
            player_hand=Hand()
            self._players[name]=[player, player_hand, playerbank]

    def take_bets(self):                    #runtime error
        for name in self._players:
            pbank=self._players[name][2]
            bet=self._players[name][0].make_bet(pbank)
            if bet>pbank.get_balance():
                raise RuntimeError("Not enough balance")
            else:
                self._players[name][2].enter_bet(bet)


    def deal_initial_hand(self):
        for name in self._players:
            card1=self._deck.remove_card()
            card2=self._deck.remove_card()
            self._players[name][1].add_card(card1)
            self._players[name][1].add_card(card2)
            self._cards_dealt.append(card1)
            self._cards_dealt.append(card2)

        card3 = self._deck.remove_card()
        card4 = self._deck.remove_card()
        self._cards_dealt.append(card3)
        self._dealer_hand.add_card(card3)
        self._dealer_hand.add_card(card4)

     # player[0] = player
        # player[1] = playerhand
        #player[2] = playerbank
    def deal_player_hands(self):   #want_card use_ace_hi
        for name in self._players:
            player=self._players[name]
            ace=player[0].use_ace_hi(player[1])
            n=player[1].score_hand(ace)
            player[1].set_score(n)
            while player[0].want_card(player[1], player[2], self._dealer_hand, self._cards_dealt)==True and n<21:
                card=self._deck.remove_card()
                self._cards_dealt.append(card)
                player[1].add_card(card)
                n=player[1].score_hand(player[0].use_ace_hi(player[1]))
                player[1].set_score(n)

            #player[1].set_score(n)
            if player[1].get_score()>21:
                player[2].bust()



    def deal_dealer_hand(self):

        n=self._dealer_hand.score_hand(self._dealer_hand.has_ace())
        self._dealer_hand.set_score(n)


        while self._dealer.want_card(None, None, self._dealer_hand, self._cards_dealt)==True:

            card=self._deck.remove_card()
            self._cards_dealt.append(card)
            self._dealer_hand.add_card(card)
            self._dealer_hand.score_hand(self._dealer_hand.has_ace())
            n = self._dealer_hand.score_hand(self._dealer_hand.has_ace())
            self._dealer_hand.set_score(n)




    def settle_bets(self):   #paywinner bust
        for name in self._players:
            player=self._players[name]
            if player[1].get_score()>21:
                player[2].bust()

            else:   #player <=21
                if self._dealer_hand.get_score()>21 or self._dealer_hand.get_score()<player[1].get_score():
                    player[2].pay_winner(2*player[2].get_wager())



    def __str__(self):
        cardlist=""

        for name in self._players:
            status=""
            if self._players[name][1].get_score()>21:
                status+="bust."
            elif self._players[name][2].get_status()==True:
                status+="winner!"
            cardlist+="\n"+"Player: "+str(name)+"\n"+str(self._players[name][1])+str(self._players[name][2])+status+"\n"
        return "$$$$$$    Game Summary   $$$$$$\n" +"Dealer: \n" +"score: "+str(self._dealer_hand.get_score())+"\n"+str(self._dealer_hand.get_cards())+"\n"+cardlist+"\n"











