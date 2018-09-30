import random
from card import Card

class Deck(list):
    """
    Represents a deck of Cards.   
    Inherits from list
    Cards are added at the end of the list: Use append
    Cards are dealt from the front of the list: Use pop
    """
    
    def __init__(self):
        """
        Be sure to call the list constructor
        """
        super().__init__()
    
    def initialize(self):    
        """
        Initialize the Deck with 52 Cards
        Both the Suits and Ranks are integers
        Suits: 0=Clubs, 1=Diamonds, 2=Hearts, 3=Spades
        Ranks: 1=Ace, 2-10=2=10, 11=Jacks, 12=Queen, 13=King
        """
        
        for suit in range(4):
            for rank in range(1,14):
                self.add_card(Card(suit, rank))
                
    def add_card(self, card):
        """
        Add the Card to the end of the list
        """
        
        self.append(card)

    def deal(self):
        """
        Removes and returns the first Card in the list
        """
        draw = self[0]
        del self[0]
        return draw

    def shuffle(self):        
        """
        The random class has a shuffle method 
        that accepts a list as an argument
        Return the shuffled Deck
        """
        
        return random.shuffle(self)
        
    def __str__(self):
        """
        Returns a string containing the list of Cards 
        in the Deck: 13 Cards to a line
        The "\n" character is added for every 13th Card
        """
        deck_str = ""
        for c in range(len(self)):
            deck_str += str(self[c]) + " "
            if  (c + 1)% 13 == 0:
                deck_str += '\n'
        return deck_str
