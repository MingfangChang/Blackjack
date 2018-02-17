class PlayerBank:
    def __init__(self, _balance, _bets_placed=0, _is_winner=False):
        self._balance=_balance
        self._bets_placed=_bets_placed
        self._is_winner=_is_winner

    def pay_winner(self, amount):
        self._balance+=amount
        self._is_winner=True

    def bust(self):
        self._is_winner=False

    def get_balance(self):
        return self._balance

    def get_wager(self):
        return self._bets_placed

    def enter_bet(self, amount ):
        if amount>self._balance:
            raise RuntimeError("Bet is greater than balance.")
        else:
            self._bets_placed+=amount
            self._balance=self._balance-amount

    def __str__(self):

        return "Player assets: \n"+"bet "+str(self.get_wager())+" balance "+str(self.get_balance())+" "

    def get_status(self):          #helper method
        return self._is_winner