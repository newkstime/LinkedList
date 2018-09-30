from card import Card
from linkedList import LinkedList

class Hand(LinkedList):
    """
    This represents a player's Hand in the card game
    It inherits from the Linked List class.
    This Hand is controlled by the Player
    The Player holds the Hand as an instance variable
    """
    def __init__(self):
        """
        Constructor:
        Be sure to call the LinkedList constructor
        """
        
        super().__init__()
        
    def __str__(self):
        """
        Returns a string containing the list of Cards 
        in the Hand: 13 Cards to a line
        The "\n" character is added for every 13th Card
        """      
        current = self._head
        hand_str = ""
        for c in range(self._size):
            hand_str += "{} ".format(current.data)
            if  (c + 1) % 13 == 0:
                hand_str += '\n'
            current = current.next
        return hand_str

    
       
