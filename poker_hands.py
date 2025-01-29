def make_deck():
    """Creates a standard deck of 52 cards as tuples (rank, suit)."""
    suits = ["c", "d", "h", "s"] # clubs, diamonds, hearts, spades
    ranks = list(range(2, 15)) # 2-10, jack (11), queen (12), king (13), ace (14)
    
    return [(rank, suit) for suit in suits for rank in ranks]
          
def main():
    deck = make_deck()
    print(deck)
          
if __name__ == "__main__":
    main()
