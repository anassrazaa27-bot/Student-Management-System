"""Grade calculation rules."""

def calculate_grade(average):
    if not 0 <= average <= 100:
        raise ValueError("Average must be between 0 and 100.")
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"
