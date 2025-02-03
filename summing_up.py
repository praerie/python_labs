def sum_n(n):
    """Returns the sum of the first n natural numbers."""
    return n * (n + 1) // 2

def sum_n_cubes(n):
    """Returns the sum of the cubes of the first n natural numbers."""
    return (n * (n + 1) // 2) ** 2

def main():
    while True:
        try:
            n = int(input("Please enter a whole number greater than 0 (no decimals or negatives): "))
        
            if n < 1:
                print("Invalid input. Enter a whole number greater than 0.")
            else: 
                print(f"Sum of the first {n} natural numbers: {sum_n(n)}")
                print(f"Sum of the cubes of the first {n} natural numbers: {sum_n_cubes(n)}")
                break # exits loop after correct input is entered and results are calculated and printed
        except ValueError:
            print("Invalid input. Enter a whole number greater than 0 (no decimals or negatives).")

if __name__ == "__main__":
    main()