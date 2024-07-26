from Suits import suits
from Ranks import ranks
class Card:
    def __init__(self, suit, rank):
        if(not(self.validateSuitAndRank(suit, rank))):
            print('Invalid Card with suit ' + str(suit) + ' ' + str(rank))
            return
        
        self.suit = suit
        self.rank = rank
    
    def validateSuitAndRank(suit, rank):
        if ((not(suit in suits)) or (not(rank in ranks))):
            return False

    def getSuit(self):
        return self.suit
    
    def getRank(self):
        return self.rank
        
    