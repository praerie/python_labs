def remove_duplicates(unique_list):
    """
    Removes duplicate items from the given list.

    Args:
        unique_list (list): Input list that may contain duplicate values.

    Returns:
        result (list): A new list with duplicates removed.
    """
    # initialize an empty set to keep track of seen items
    seen = set()
    
    # initialize an empty list to store unique items in the order they appear
    result = []
    
    for item in unique_list:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

def main():
    herbs = ["thyme", "sumac", "tarragon", "dill", "dill", "black pepper", "sumac", "marjoram"]
    studios = ["Dreamworks", "Nickelodeon", "Disney", "Sony", "Sony", "ILM", "Animal Logic", "ILM", "ILM"]
    hobbies = ["archery", "archery", "archery", "knitting", "language learning", "mountain biking"]

    print("original list of herbs:", herbs)
    print("post duplicate removal:", remove_duplicates(herbs), "\n")

    print("original list of studios", studios)
    print("post duplicate removal:", remove_duplicates(studios), "\n")

    print("original list of hobbies:", hobbies)
    print("post duplicate removal:", remove_duplicates(hobbies))

if __name__ == "__main__":
    main()


