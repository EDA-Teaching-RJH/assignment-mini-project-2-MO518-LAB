import re  # Required for regular expressions
import csv  # Library for File I/O
import unittest  # For testing functionality


# Creating a custom library with utility functions
class UniversityLibrary:
    def __init__(self):
        self.students = []

    def add_student(self, name, student_id, email):
        if not re.match(r"^[a-zA-Z]+$", name):
            raise ValueError("Name must contain only alphabets")
        if not re.match(r"^\d{4}$", student_id):
            raise ValueError("Student ID must be a 4-digit number")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format")
        self.students.append({"name": name, "student_id": student_id, "email": email})


# File I/O operations: Saving and reading student data
class FileOperations:
    @staticmethod
    def save_students_to_file(filename, students):
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["name", "student_id", "email"])
            writer.writeheader()
            writer.writerows(students)

    @staticmethod
    def read_students_from_file(filename):
        with open(filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader]


# Object-Oriented Programming: Base and derived classes
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Student(Person):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id


# Unit testing for the functionality
class TestUniversitySystem(unittest.TestCase):
    def test_add_student(self):
        lib = UniversityLibrary()
        lib.add_student("Damilola", "2508", "dh492@kent.ac.uk")
        self.assertEqual(len(lib.students), 1)

    def test_invalid_student_name(self):
        lib = UniversityLibrary()
        with self.assertRaises(ValueError):
            lib.add_student("Damilola250", "2508", "dh492@kent.ac.uk")

    def test_file_operations(self):
        students = [
            {"name": "Michael", "student_id": "2401", "email": "mo518@kent.ac.uk"},
            {"name": "Emmanuel", "student_id": "2340", "email": "eg234@kent.ac.uk"},
        ]
        FileOperations.save_students_to_file("students.csv", students)
        loaded_students = FileOperations.read_students_from_file("students.csv")
        self.assertEqual(students, loaded_students)


if __name__ == "__main__":
    # Example usage
    university = UniversityLibrary()
    university.add_student("Michael", "2401", "mo518@kent.ac.uk")
    university.add_student("Emmanuel", "2340", "eg234@kent.ac.uk.")
    print("Students added:", university.students)

    # Save to a file
    FileOperations.save_students_to_file("students.csv", university.students)

    # Read back from the file
    students_from_file = FileOperations.read_students_from_file("students.csv")
    print("Students loaded from file:", students_from_file)

    # Run tests
    unittest.main()
