def make_deck():
    """Creates a standard deck of 52 cards as tuples (rank, suit)."""
    suits = ["c", "d", "h", "s"] # clubs, diamonds, hearts, spades
    ranks = list(range(2, 15)) # 2-10, jack (11), queen (12), king (13), ace (14)
    
    return [(rank, suit) for suit in suits for rank in ranks]

def count_cards(cards):
    # return True if hand contains exactly 5 cards
    return len(cards) == 5 

def straight_flush(cards):
    """Returns true if hand has five ranks in a row of all the same suit."""
    # verify that hand contains exactly 5 cards
    if not count_cards(cards):
        return False
    
    # create a set of unique suits from list of card tuples
    suits = {suit for _, suit in cards}
    
    if len(suits) > 1:
        return False # must be same suit
    
    # unpack and sort ranks
    ranks = [rank for rank, _ in cards]
    ranks.sort()
    
    # return True if hand has consecutive ranks
    return all(ranks[i] + 1 == ranks[i + 1] for i in range(len(ranks) - 1))

def four_of_a_kind(cards):
    """Returns true if hand has four of the same rank."""
    # verify that hand contains exactly 5 cards
    if not count_cards(cards):
        return False
    
    # create a dictionary to store counts of each rank
    rank_counts = {}
    
    # count occurrences of each rank using .get(key, default)
    for rank, _ in cards:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
    
    # return True if any rank appears exactly 4 times
    return 4 in rank_counts.values()

def full_house(cards):
    """Returns true if hand has three of one rank and two of another."""
    # verify that hand contains exactly 5 cards
    if not count_cards(cards):
        return False
    
    # create a dictionary to store counts of each rank
    rank_counts = {}
    
    # count occurrences of each rank using .get(key, default)
    for rank, _ in cards:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
        
    # return True if hand contains 2 distinct ranks with counts 2 and 3
    return len(rank_counts) == 2 and sorted(rank_counts.values()) == [2, 3]

def flush(cards):
    """Returns true if hand has five cards of the same suit."""
    # verify that hand contains exactly 5 cards
    if not count_cards(cards):
        return False
    
    # create a set of unique suits from list of card tuples
    suits = {suit for _, suit in cards}
    
    # return True if each card shares the same suit
    return len(suits) == 1

def straight(cards):
    """Returns true if hand has five ranks in a row."""
    # verify that hand contains exactly 5 cards
    if not count_cards(cards):
        return False
    
    # unpack and sort ranks
    ranks = [rank for rank, _ in cards]
    ranks.sort()
    
    # return True if hand has consecutive ranks
    return all(ranks[i] + 1 == ranks[i + 1] for i in range(len(ranks) - 1))

def three_of_a_kind(cards):
    """Returns true if hand has three of one rank,
    but not a full house nor four of a kind."""
    # verify that hand contains exactly 5 cards
    if not count_cards(cards):
        return False
    
    # create a dictionary to store counts of each rank
    rank_counts = {}
    
    # count occurrences of each rank using .get(key, default)
    for rank, _ in cards:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
        
    # return True if hand contains 3 cards of one rank,
    # and 1 of two different ranks (excluding full house and four of a kind)
    return sorted(rank_counts.values()) == [1, 1, 3]

def two_pair(cards):
    """Returns true if hand has two each of two different ranks."""
    # verify that hand contains exactly 5 cards
    if not count_cards(cards):
        return False
    
    # create a dictionary to store counts of each rank
    rank_counts = {}
    
    # count occurrences of each rank using .get(key, default)
    for rank, _ in cards:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1

    # return True if hand contains exactly two pairs of the same rank and one unmatched card
    return sorted(rank_counts.values()) == [1, 2, 2]

def pair(cards):
    """Returns true if hand has two of the same rank,
    but not two pair, three, or four of a kind."""
    # verify that hand contains exactly 5 cards
    if not count_cards(cards):
        return False
    
    # create a dictionary to store counts of each rank
    rank_counts = {}
    
    # count occurrences of each rank using .get(key, default)
    for rank, _ in cards:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
        
    # return True if hand contains exactly one pair of the same rank and two unmatched cards
    return sorted(rank_counts.values()) == [1, 1, 1, 2]
          
def main():
    deck = make_deck()
    print(f"standard 52-card deck: {deck}")
    
    # test cases that should evaluate to True
    hand_straight_flush = [(2, "s"), (4, "s"), (6, "s"), (5, "s"), (3, "s")]
    hand_four_of_a_kind = [(7, "c"), (7, "h"), (7, "d"), (7, "s"), (3, "c")]
    hand_full_house = [(12, "d"), (12, "h"), (12, "s"), (9, "h"), (9, "d")]
    hand_flush = [(11, "s"), (7, "s"), (2, "s"), (8, "s"), (3, "s")]
    hand_straight = [(10, "d"), (9, "s"), (8, "h"), (7, "c"), (6, "c")]
    hand_three_of_a_kind = [(7, "d"), (7, "c"), (7, "s"), (4, "h"), (10, "c")]
    hand_two_pair = [(2, "d"), (2, "s"), (9, "s"), (9, "h"), (11, "c")]
    hand_pair = [(7, "d"), (7, "c"), (2, "s"), (14, "h"), (12, "h")]
    
    # test cases that should evaluate to False
    hand_not_straight_flush = [(2, "s"), (4, "s"), (6, "s"), (5, "s"), (8, "s")]  # not consecutive
    hand_not_four_of_a_kind = [(7, "c"), (7, "h"), (7, "d"), (3, "s"), (3, "c")]  # full house
    hand_not_full_house = [(12, "d"), (12, "h"), (12, "s"), (9, "h"), (8, "d")]  # three of a kind + random cards
    hand_not_flush = [(11, "s"), (7, "s"), (2, "s"), (8, "s"), (3, "h")]  # one card of a different suit
    hand_not_straight = [(10, "d"), (9, "s"), (8, "h"), (7, "c"), (5, "c")]  # missing consecutive rank
    hand_not_three_of_a_kind = [(7, "d"), (7, "c"), (4, "s"), (4, "h"), (10, "c")]  # two pair instead
    hand_not_two_pair = [(2, "d"), (2, "s"), (9, "s"), (8, "h"), (11, "c")]  # only one pair
    hand_not_pair = [(7, "d"), (6, "c"), (2, "s"), (14, "h"), (12, "h")]  # no pairs at all

    print("——————— TRUE TEST CASES (should return True) ———————")
    print(f"straight flush: {hand_straight_flush}, {straight_flush(hand_straight_flush)}")
    print(f"four of a kind: {hand_four_of_a_kind}, {four_of_a_kind(hand_four_of_a_kind)}")
    print(f"full house: {hand_full_house}, {full_house(hand_full_house)}")
    print(f"flush: {hand_flush}, {flush(hand_flush)}")
    print(f"straight: {hand_straight}, {straight(hand_straight)}")
    print(f"three of a kind: {hand_three_of_a_kind}, {three_of_a_kind(hand_three_of_a_kind)}")
    print(f"two pair: {hand_two_pair}, {two_pair(hand_two_pair)}")
    print(f"pair: {hand_pair}, {pair(hand_pair)}")
          
    print("——————— FALSE TEST CASES (should return False) ———————")
    print(f"not straight flush: {hand_not_straight_flush}, {straight_flush(hand_not_straight_flush)}")
    print(f"not four of a kind: {hand_not_four_of_a_kind}, {four_of_a_kind(hand_not_four_of_a_kind)}")
    print(f"not full house: {hand_not_full_house}, {full_house(hand_not_full_house)}")
    print(f"not flush: {hand_not_flush}, {flush(hand_not_flush)}")
    print(f"not straight: {hand_not_straight}, {straight(hand_not_straight)}")
    print(f"not three of a kind: {hand_not_three_of_a_kind}, {three_of_a_kind(hand_not_three_of_a_kind)}")
    print(f"not two pair: {hand_not_two_pair}, {two_pair(hand_not_two_pair)}")
    print(f"not pair: {hand_not_pair}, {pair(hand_not_pair)}")

if __name__ == "__main__":
    main()

