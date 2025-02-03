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

import random

class PlayingCard: 
    SUITS = {"d": "Diamonds", "c": "Clubs", "h": "Hearts", "s": "Spades"}
    RANKS = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit
    
    def blackjack_value(self):
        if self.rank == 1:
            return 1 # ace is worth 1 in blackjack
        elif self.rank in {11, 12, 13}:
            return 10 # face cards are worth 10 (jack, queen, king)
        return self.rank # number cards keep their value
    
    def __str__(self):
        rank_name = self.RANKS.get(self.rank, self.rank) # assigns "Ace" or face card name, otherwise rank number
        suit_name = self.SUITS[self.suit] # retrieves full name from SUITS dictionary
        return f"{rank_name} of {suit_name}"

    @classmethod
    def create_deck(cls):
        """Creates a standard deck of 52 playing cards."""
        return [cls(rank, suit) for suit in cls.SUITS for rank in range(1, 14)]
    
def main():
    deck = PlayingCard.create_deck()
    
    print("Engaging quantum card entanglement... Shuffle matrix loaded... Input interface activated.")
    
    while True:
        try:
            n_cards = int(input("# of cards to display (1-52): "))

            if n_cards == 0:
                print("Ah, the mystical art of drawing zero cards! A bold choice... but rather uneventful.")
            elif n_cards < 0:
                print("Ah, attempting to summon negative cards, are we? "\
                      "Alas, they exist only in the void and hold no Blackjack value.")
            elif n_cards > 52:
                print("My human maker, bound by the laws of earthly decks, has granted me only 52 cards. No more, no less!")
            else:
                random_selection = random.sample(deck, n_cards) # randomly select n cards from deck
                for card in random_selection:
                    print(f"{card} is worth {card.blackjack_value()} in Blackjack.")
                break # exit after displaying n random cards 
        except ValueError:
            print("ERROR: Anomaly detected. Resetting card-drawing matrix... Please enter a number between 1 and 52.")


if __name__ == "__main__":
    main()
