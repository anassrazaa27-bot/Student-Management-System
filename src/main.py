"""Command-line interface for the Student Performance Management System."""
from src.student import Student, StudentRepository, SUBJECTS
from src.grading import calculate_grade

def read_marks():
    marks = {}
    for subject in SUBJECTS:
        while True:
            try:
                value = float(input(f"Enter {subject} marks (0-100): "))
                if not 0 <= value <= 100:
                    print("Marks must be between 0 and 100.")
                    continue
                marks[subject] = value
                break
            except ValueError:
                print("Please enter a valid number.")
    return marks

def print_report(student):
    print("\n" + "=" * 44)
    print("           STUDENT PERFORMANCE REPORT")
    print("=" * 44)
    print(f"Student ID : {student.student_id}")
    print(f"Name       : {student.name}")
    for subject in SUBJECTS:
        print(f"{subject:<12}: {student.marks[subject]:.2f}")
    print("-" * 44)
    print(f"Total      : {student.total:.2f} / 500")
    print(f"Average    : {student.average:.2f}%")
    print(f"Grade      : {calculate_grade(student.average)}")
    print("=" * 44)

def add_student(repository):
    print("\n--- Register New Student ---")
    student_id = input("Student ID: ").strip()
    name = input("Student name: ").strip()
    if not student_id or not name:
        print("Student ID and name cannot be empty.")
        return
    if repository.find(student_id):
        print("This student ID already exists.")
        return
    marks = read_marks()
    repository.save(Student(student_id, name, marks))
    print(f"Student {name} saved successfully.")

def search_student(repository):
    student_id = input("\nEnter student ID to search: ").strip()
    student = repository.find(student_id)
    if student:
        print_report(student)
    else:
        print("No student found with that ID.")

def show_top_performer(repository):
    students = repository.get_all()
    if not students:
        print("No student records available yet.")
        return
    top = max(students, key=lambda student: student.average)
    print("\n--- Top Performer ---")
    print_report(top)

def list_students(repository):
    students = repository.get_all()
    if not students:
        print("\nNo student records available yet.")
        return
    print("\n{:<14} {:<24} {:>10} {:>8}".format("STUDENT ID", "NAME", "AVERAGE", "GRADE"))
    print("-" * 60)
    for student in students:
        print("{:<14} {:<24} {:>9.2f}% {:>8}".format(
            student.student_id, student.name[:24], student.average,
            calculate_grade(student.average)))

def main():
    repository = StudentRepository()
    while True:
        print("\n" + "=" * 48)
        print("     STUDENT PERFORMANCE MANAGEMENT SYSTEM")
        print("=" * 48)
        print("1. Add student and marks")
        print("2. Search student by ID")
        print("3. Show top performer")
        print("4. List all students")
        print("5. Exit")
        choice = input("\nChoose an option (1-5): ").strip()
        if choice == "1":
            add_student(repository)
        elif choice == "2":
            search_student(repository)
        elif choice == "3":
            show_top_performer(repository)
        elif choice == "4":
            list_students(repository)
        elif choice == "5":
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 to 5.")

if __name__ == "__main__":
    main()
