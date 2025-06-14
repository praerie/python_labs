low, high = 1, 15

for _ in range(4):  # At most 4 guesses
    guess = (low + high) // 2
    print(f"Is x = {guess}?")

    response = input().strip()  # Assume input is given as "Yes", "x < y", or "x > y"

    if response == "Yes":
        print(f"Found x! It is {guess}.")
        break
    elif response == "x < y":
        high = guess - 1  # Reduce search space
        print(high)
    elif response == "x > y":
        low = guess + 1  # Increase search space
        print(low)
