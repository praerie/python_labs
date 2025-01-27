def get_grade(score):
    """
    Calculate letter grade using a standard 100-point scale.
    
    Logic:
    - Grades lookup string ("FDCBA") represents grade letters in reverse order.
    - 'score - 50' shifts scoring range into 10-point intervals:
        - A (90-100): (90 - 50) // 10 = 4
        - B (80-89): (80 - 50) // 10 = 3
        - C (70-79): (70 - 50) // 10 = 2
        - D (60-69): (60 - 50) // 10 = 1
        - F (0-59): (0 - 50) // 10 = -5, clamped to 0 by max()
        
    Args:
        score (int): Exam score between 0 and 100.
    
    Returns:
        str: Corresponding grade letter.
    """
    grades = "FDCBA"

    index = max(0, (score - 50) // 10)  
    return grades[index]

def main():
    try:
        score = int(input("Enter the exam score (0-100): "))
        if 0 <= score <= 100:
            print(f"Grade letter: {get_grade(score)}")
        else:
            print("Score is out of range (0-100).")
    except ValueError:
        print("Invalid score. Please enter a valid numeric value (0-100).")

if __name__ == "__main__":
    main()