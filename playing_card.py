# Implement a class to represent a playing card with the following methods:
#
# __init__(self, rank, suit)
# get_rank(self) returns the rank of the card
# get_suit(self) returns the suit of the card
# blackjack_value(self) returns the blackjack value of a card; ace counts as 1, and face cards count as 10.
# __str__(self) returns a string that names the card, e.g. "Ace of Spades"
#
# Test your card class with a program that prints out n randomly generated cards
# and the associated Blackjack value where n is a number supplied by the user.

class PlayingCard: 
    SUITS = ["d", "c", "h", "s"]
    RANKS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit
    
    def blackjack_value(self):
        pass
    
    def __str__(self):
        suit_name = ""
        rank_name = ""

        if self.suit == "d":
            suit_name = "Diamonds"
        elif self.suit == "c":
            suit_name = "Clubs"
        elif self.suit == "h":
            suit_name = "Hearts"
        elif self.suit == "s":
            suit_name = "Spades"

        if self.rank == 11:
            rank_name = "Jack"
        elif self.rank == 12:
            rank_name = "Queen"
        elif self.rank == 13:
            rank_name = "King"
        elif self.rank == 1:
            rank_name = "Ace"
        else:
            rank_name = self.rank
        
        return f"{rank_name} of {suit_name}"

    @classmethod
    def create_deck(cls):
        """Creates a standard deck of 52 playing cards."""
        return [cls(rank, suit) for suit in cls.SUITS for rank in cls.RANKS]
    
def main():
    deck = PlayingCard.create_deck()
    print(deck[2])

if __name__ == "__main__":
    main()