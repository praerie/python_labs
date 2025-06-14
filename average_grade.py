def student_averages(grades_dict):
    averages = {}  # dictionary to store average for each student

    for student, subjects in grades_dict.items():
        # sum up all grades for the student
        total = sum(subjects.values())
        count = len(subjects)
        # compute average, avoiding division by zero
        averages[student] = total / count if count else 0
    return averages

def main():
    # sample input of student grades
    grades = {
        "Alvin": {"Math": 90, "Science": 80, "History": 65},
        "Simon": {"Math": 75, "Science": 85, "History": 70},
        "Theodore": {"Math": 98, "Science": 73, "History": 82}
    }

    averages = student_averages(grades)
    for student, avg in averages.items():
        print(f"{student}'s average: {avg:.2f}")

if __name__ == "__main__":
    main()
