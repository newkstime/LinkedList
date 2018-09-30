from card import Card
from linkedList import LinkedList

class Pile(LinkedList):
    """
    Represents a pile of Cards on the Table
    Inherits from Linked List
    Cards are added at the front of the Pile
    """
    def __init__(self):
        """
        Constructor:
        Be sure to call the LinkedList constructor
        """
        
        super().__init__()
        
    def add_card(self, card):
        """
        Add the Card to the front of the list
        """
        
        self.add_first(card)

    def top_two_cards(self):
        """
        Find the first two nodes and
        return the Node data containing the Cards
        Return Player1 Card, Player2 Card
        """
        
        player1_card = self._head
        player2_card = self._head.next
        return player1_card.data, player2_card.data

    def __str__(self):
        """
        Return the Cards in the pile as a string
        starting with the first Card as:
         Rank-Suit Rank-Suit Rank-Suit etc
        """
        current = self._head
        pile_str = ""
        for c in range(self._size):
            pile_str += "{} ".format(current.data)
            if  (c + 1)% 13 == 0:
                pile_str += '\n'
            current = current.next
        return pile_str
