def student_averages(grades_dict):
    averages = {}  # dictionary to store average for each student

    for student, subjects in grades_dict.items():
        # sum up all grades for the student
        total = sum(subjects.values())
        count = len(subjects)
        # compute average, avoiding division by zero
        averages[student] = total / count if count else 0
    return averages

def subject_averages(grades_dict):
    subject_totals = {}  # total grades for each subject
    subject_counts = {}  # count of grades for each subject

    for subjects in grades_dict.values():
        for subject, grade in subjects.items():
            # add grade to the total for that subject
            subject_totals[subject] = subject_totals.get(subject, 0) + grade
            # increment the count of grades for that subject
            subject_counts[subject] = subject_counts.get(subject, 0) + 1

    averages = {}
    for subject in subject_totals:
        # compute average for each subject
        averages[subject] = subject_totals[subject] / subject_counts[subject]
    return averages

def main():
    # sample input of student grades
    grades = {
        "Alvin": {"Math": 90, "Science": 80, "History": 65},
        "Simon": {"Math": 75, "Science": 85, "History": 70},
        "Theodore": {"Math": 98, "Science": 73, "History": 82}
    }

    # compute and print average per student
    print("Student Averages:")
    averages = student_averages(grades)
    for student, avg in averages.items():
        print(f"{student}'s average: {avg:.2f}")

    # compute and print average per subject across the class
    print("\nClass Averages by Subject:")
    subject_avg = subject_averages(grades)
    for subject, avg in subject_avg.items():
        print(f"{subject}: {avg:.2f}")

if __name__ == "__main__":
    main()
