students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]


def calculate_average(marks):
    total = 0
    for mark in marks:
        total = total + mark
    return total / len(marks)


def classify_performance(average):
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


def is_valid_marks(marks):
    if len(marks) == 0:
        return False

    for mark in marks:
        if mark < 0 or mark > 100:
            return False
    return True


def display_report(students):
    for student in students:
        marks = student[2]
        if not is_valid_marks(marks):
            print(student[0], student[1], "- invalid or missing marks, skipped")
        else:
            average = calculate_average(marks)
            print(student[0], student[1], "Average:", round(average, 2), classify_performance(average))


# Testing
print("--- Sample report ---")
display_report(students)

print("--- Equal marks, tied averages, invalid mark, no marks ---")
display_report([
    [206, "Equal", [70, 70, 70]],
    [207, "Tie A", [60, 80, 70]],
    [208, "Tie B", [70, 70, 70]],
    [209, "Invalid", [50, 150, 60]],
    [210, "Missing", []]
])
