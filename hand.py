class Hand:
    def __init__(self):
        self._cards=[]
        self._score=0

    def add_card(self, card):
        self._cards.append(card)

    def get_score(self):
        return self._score

    def set_score(self, score):
        self._score=score

    def has_ace(self):
        num=0
        for c in self._cards:
            if c[0]=='A':
                num+=1
        if num!=0:
            return True
        else:
            return False


    def score_hand(self, b):
        num=0

        for c in self._cards:
            if c[0]=='J' or c[0]=='Q' or c[0]=='K':
                num+=10
            if c[0]=='2' or c[0]=='3' or c[0]=='4' or c[0]=='5' or c[0]=='6' or c[0]=='7' or c[0]=='8' or c[0]=='9' or c[0]=='10':
                num+=int(c[0])
            if b==True and c[0]=='A' :
                num+=11
            if b==False and c[0]=='A':
                num+=1
            #self.set_score(num)

        return num

    def get_cards(self):
        return self._cards

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        return "score: "+str(self.get_score())+"\n"+str(self.get_cards())+"\n"


