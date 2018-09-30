from deck import Deck
from card import Card
from coin import Coin
from player import Player
from hand import Hand
from pile import Pile

class Broker():
    """
    This class plays the Buy, Sell, or Negotiate card game. 
    It has a Deck, a Pile and twp Players as instance variables.  
    It also contains an instance variable for counting the number 
    of rounds and negotiations and which Player won them. 
    It contains an optional parameter that you can set to stop 
    the play after a certain number of rounds, called limit..
    """

    def __init__(self, limit = 1000):
        """
        Initialize round limit
        Initialize the Deck and Pile
        Create both Players and place in list
        Create the lists holding the round and negotiation counts
        """
        # 1. Initialize round limit
        
        self.__limit = limit
        
        # 2. Initialize the Deck and Pile
        
        self.__deck = Deck()
        self.__pile = Pile()
        
        # 3. Create both Players and place in list
        
        self.__players = [None, Player(), Player()]
        
        # 4. Create the lists holding the round and negotiation counts
        
        self.__round_wins = [0, 0, 0]

    def setup(self):
        """
        Initialize the Deck
        Shuffle the Deck 5 times and display it
        Deal the cards
        Display the dealt hands 
        """
    
        print("=============SETUP===============")
                    
        # 1. Initialize the Deck
        
        print("The new deck:")
        self.__deck.initialize() 

        # 2. Shuffle the Deck 5 times and display it
        
        for d in range(5):
            self.__deck.shuffle()
        print("The shuffled deck:")   
        print(self.__deck)
         
        # 3. Deal the cards
        
        for c in range(26):
            for p in range(1,3):
                card = self.__deck.deal()
                player = self.__players[p]
                player.add_card(card)
        
        # 4. Display the dealt hands 
                
        print("Original hands:")
        for p in range(1,3):
            player = self.__players[p]
            print("Player{}:".format(p))
            player.display_hand()
 
           
    def play(self):
        """
        Loop for each round of play
        Game ends when someone wins or after round limit
        1. Each player plays a Card to the pile
           Display the first two top Cards on the Pile
        2. Call determine_pile_winner to determine the winner
           Winner is returned as player number (1 or 2) 
           or 0, if cards are equal
        3. If Cards are equal,
           winner is determined through negotiation
           If Cards are not equal, winner gets pile
           A. Cards are equal: 
              If both players have at least one Card, 
              Call negotiate to determine winner
           B. One player does not have enough Cards,
              use Coin flip to see if he survives
        4. Cards are not equal: winning Player adds Pile to Hand
        5. Check for game over: meaning a Player has no Cards
        6. Increment the number of rounds
        """
        print("=============== PLAY ===============")
        
        rounds = 1
        game_over = False
         
        # Loop for each round of play
        # Game ends when someone wins or after round limit
        
        while not game_over and rounds <= self.__limit:
            
            print("\nRound{}: ".format(rounds))
            
            # 1. Each player plays a Card to the pile
            #    Display the first two top Cards on the Pile
             
            for p in range(1,3):
                player = self.__players[p]
                player.play_card(self.__pile)
                    
            p1_card, p2_card = self.__pile.top_two_cards()

            print("Player1: Card: " + str(p1_card))
            print("Player2: Card: " + str(p2_card))
        
            # 2. Call determine_pile_winner to determine the winner
            #    Winner is returned as player number (1 or 2) 
            #    or 0, if cards are equal
                         
            winner = self.determine_pile_winner()
            print("Winner: Player" + str(winner))
            
            # 3. If Cards are equal,
            #    winner is determined through negotiation
            #    If Cards are not equal, winner gets pile
                
            if winner == 0:
                print("\nLet the NEGOTIATIONs Begin!!!")

                # A. Cards are equal: 
                #    If both players have at least one Card, 
                #    Call negotiate to determine winner

                p1_num_cards = self.__players[1].get_num_cards()
                p2_num_cards = self.__players[2].get_num_cards()
                
                if (p1_num_cards >= 1) and (p2_num_cards >= 1):
                    winner = self.negotiate()
                    
                    print("Winner: Player" + str(winner))
                    if winner == 0:
                       game_over = self.use_coin_flip_for_neg()
                    else:
                        self.__players[winner].add_pile(self.__pile)

                # B. One player does not have enough Cards,
                #    use Coin flip to see if he survives
                else:
                    game_over = self.use_coin_flip_for_neg()

            # 4. Cards are not equal: winning Player adds Pile to Hand
            
            else:
                self.__players[winner].add_pile(self.__pile)

            self.__round_wins[0] += 1
            self.__round_wins[winner] += 1
            
            # 5. Check for game over: meaning a Player has no Cards
            
            if (self.__players[1].get_num_cards() == 0 or
                self.__players[2].get_num_cards() == 0):
                game_over = True 
        
            # 6. Increment the number of rounds
            
            rounds += 1
            

    def determine_pile_winner(self):
        """
        1. Retrieve the top two Cards from the Pile
        2. Compare the Cards:
           A. Cards are equal: 
              Return winner = 0 
           B. Flip Coin to see whether the low Card 
              or the high Card wins the play
              1. If the flip is heads, make high card holder the winner
              2. If the flip is tails, make low card holder the winner
        """
        # 1. Retrieve the top two Cards from the Pile

        p1_card, p2_card = self.__pile.top_two_cards()
        
        # 2. Compare the Cards:
        
        compare_result = p1_card.compare(p2_card)
        
        if compare_result == 0:
        
            # A. Cards are equal: 
            #    Return winner = 0 
    
            return 0 
                
        else:
        
            # B. Flip Coin to see whether the low Card 
            #    or the high Card wins the play

            face = Coin().flip()
            print("Face: {}".format(face))
             
                # 1. If the flip is heads, make high card holder the winner
             
            if face == "Heads":
            
                if compare_result > 0:
                    return 1
                else:
                    return 2
        
                # 2. If the flip is tails, make low card holder the winner
            
            else:
                if compare_result > 0:
                    return 2
                else:
                    return 1
 
    def negotiate(self):
        """
        Continue the negotiations until there is a clear winner
        A clear winner means that determine_pile_winner returns 1 or 2
        """    
        # Continue the negotiations until there is a clear winner
        # Clear winner means that determine_pile_winner returns 1 or 2

        winner = 0
        while winner == 0:
        
            # 1. Each player plays four Cards for the Pile,
            #    as long as both players have Cards

            low_on_cards = False
            for c in range(4):
            
                if (self.__players[1].get_num_cards() >= 1 and
                    self.__players[2].get_num_cards() >= 1):

                    for p in range(1,3):
                        player = self.__players[p]
                        player.play_card(self.__pile)
                    
                    # Display the first two top Cards on the Pile
                        
                    p1_card, p2_card = self.__pile.top_two_cards()

                    print("Player1: Card: " + str(p1_card))
                    print("Player2: Card: " + str(p2_card))

                else:
                    low_on_cards = True
                    break
                
            # Check the last Card played to see who wins the negotiation
                 
            winner = self.determine_pile_winner()
            if winner == 0 and low_on_cards:
                break
                
        return winner

    def use_coin_flip_for_neg(self):
        """
        Use a Coin flip to determine who gets the Pile of Cards, 
        when one of the Players has only one Card and the game is in
        negotiation: Tails gives the Pile to the Player with the low
        Card number, keeping him in the game.  Heads gives the Pile 
        to the Player with the most Cards and that Player wins the game
        """

        game_over = False

        print("Using coin flip to settle negotiation")
        face = Coin().flip()
        print("Face: " + str(face))

        p1_num_cards = self.__players[1].get_num_cards()
        p2_num_cards = self.__players[2].get_num_cards()

        # 1. If the flip is Heads, the player
        #    with the most cards wins and
        #    adds the Pile of Cards to his Hand

        if face == "Heads":
            game_over = True

            if p1_num_cards < p2_num_cards:
                winner = 2
            else:
                winner = 1
            self.__players[winner].add_pile(self.__pile)

        # 2. If the flip is Tails, the player with the
        #    least cards adds the Pile of Cards to his Hand

        else:
            p1_num_cards = self.__players[1].get_num_cards()
            p2_num_cards = self.__players[2].get_num_cards()

            if p1_num_cards > p2_num_cards:
                winner = 2
            else:
                winner = 1

            self.__players[winner].add_pile(self.__pile)
        return game_over

    
    def display_results(self):
        """
        Displays the game results
        """
        print()                
        print("========== Game Over - show results ============")

        print()
        print("Number of Rounds:", self.__round_wins[0])
        print("Number of Rounds won by Player 1:", self.__round_wins[1])
        print("Number of Rounds won by Player 2:", self.__round_wins[2])

        # 1. The game ends when the round limit is reached, 
        #    or a player is out of Cards
        
        p1_num_cards = self.__players[1].get_num_cards()
        p2_num_cards = self.__players[2].get_num_cards()

        winner = 0
        if self.__round_wins[0] >= self.__limit:
        
            # A. Round limit was reached,
            #    The winner is the one with the most Cards
            
            print("Round limit of {} rounds reached".format(self.__limit))
            
            if p1_num_cards == p2_num_cards:
                    
                print("Game is tied")
                       
            else:
                if p1_num_cards > p2_num_cards:
                    winner = 1
                else:
                    winner = 2
                
                print("Player{} has won the game".format(winner))
        else:
        
            # B. A player is out of Cards
            #    The winner is the one with all the Cards

            if p1_num_cards > p2_num_cards:
                winner = 1
            else:
                winner = 2
            
            print("Player{} has won the game".format(winner))    
                        
        # 2. Display Hands, if both players have Cards    
        
        if winner == 0 or self.__players[winner].get_num_cards() < 52:
            
            for p in range(1,3):
                print("Player{} Cards:".format(p))
                self.__players[p].display_hand()
                print()


