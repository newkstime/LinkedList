from hand import Hand
from pile import Pile

class Player:
    """
    This represents a Player of the card game
    The Player holds his Hand as an instance variable, 
    The Hand is a Linked List of Cards
    When a player is dealt a card from the Deck, 
      the Card is added first in his Hand
    When a player adds a Pile after becoming the winner,
      the Pile of Cards are added last to the Hand.
    Cards are only played from the front of the Hand
    """
    def __init__(self):
        """
        Constructor:
        Create the empty hand
        """
        self._hand = Hand()
        
    def add_card(self, card):
        """
        Add the passed in Card to the Hand
        """
        
        self._hand.add_first(card)
         
    def add_pile(self, pile):
        """
        Add the passed in Pile of Cards to the Hand
        """
        
        for c in range(pile.get_size()):
            card = pile.remove_first()
            self._hand.add_last(card)
         
    def play_card(self, pile):
        """
        Remove the top Card from the Hand
        And add it to the passed in Pile
        """
        
        pile.add_card(self._hand.remove_first())
        
    def get_num_cards(self):
        """
        Return the number of Cards in the Hand
        """
        
        return self._hand.get_size()
        
    def display_hand(self):
        """
        Print the Player's Hand by calling the Hand's __str__ method
        """
        
        print (self._hand)

