"""Student model and CSV persistence."""
from dataclasses import dataclass
from pathlib import Path
import csv

SUBJECTS = ["English", "Mathematics", "Computer", "Physics", "Chemistry"]

@dataclass
class Student:
    student_id: str
    name: str
    marks: dict

    @property
    def total(self):
        return sum(self.marks.values())

    @property
    def average(self):
        return self.total / len(SUBJECTS)

    def to_dict(self):
        row = {"student_id": self.student_id, "name": self.name}
        row.update({subject: self.marks[subject] for subject in SUBJECTS})
        return row

class StudentRepository:
    """Loads and saves student records in a CSV file."""
    def __init__(self, file_path="data/students.csv"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.file_path.exists():
            self._write_all([])

    def get_all(self):
        students = []
        with self.file_path.open("r", newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                marks = {subject: float(row[subject]) for subject in SUBJECTS}
                students.append(Student(row["student_id"], row["name"], marks))
        return students

    def save(self, student):
        students = self.get_all()
        if any(s.student_id == student.student_id for s in students):
            raise ValueError("A student with this ID already exists.")
        students.append(student)
        self._write_all(students)

    def find(self, student_id):
        return next((s for s in self.get_all() if s.student_id == student_id), None)

    def _write_all(self, students):
        fieldnames = ["student_id", "name", *SUBJECTS]
        with self.file_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                writer.writerow(student.to_dict())
