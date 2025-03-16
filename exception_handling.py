class CustomError1(Exception):
    """Exception raised for division by zero."""
    pass

class CustomError2(Exception):
    """Exception raised when a file is not found."""
    pass

class CustomError3(Exception):
    """Exception raised for accessing an out-of-range index."""
    pass

def divide_numbers(a, b):
    """Divides first input by second input, handling division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        raise CustomError1("Cannot divide by zero.")

def open_file(filename):
    """Opens a file and tries to open it, handling file not found error."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise CustomError2(f"File '{filename}' not found.")

def process_data(data_list, index):
    """Accesses an element in a specific index, handling index out of range."""
    try:
        return data_list[index]
    except IndexError:
        raise CustomError3("Index out of range.")

def main():
    # Demonstration of divide_numbers function
    try:
        print(divide_numbers(10, 0))
    except CustomError1 as e:
        print(f"Error: {e}")
    
    # Demonstration of open_file function
    try:
        print(open_file("nonexistent.txt"))
    except CustomError2 as e:
        print(f"Error: {e}")
    
    # Demonstration of process_data function
    try:
        print(process_data([1, 2, 3], 5))
    except CustomError3 as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    
