class Student:
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades
    
    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def has_passed(self, passing_grade):
        return self.calculate_average() >= passing_grade


class University:
    def __init__(self, name, passing_grade):
        self.name = name
        self.passing_grade = passing_grade
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            raise TypeError("Only objects of type 'Student' can be added.")

# Example usage
if __name__ == "__main__":
    # Create some students
    student1 = Student("Michael", 24015708, [78, 89, 85])
    student2 = Student("Damilola", 23042781, [60, 65, 58])
    student3 = Student("Samuel", 25679032, [95, 92, 88])

    # Create a university
    university = University("Tech University", passing_grade=70)

    # Add students to the university
    university.add_student(student1)
    university.add_student(student2)
    university.add_student(student3)

    def list_students(self):
        return [student.name for student in self.students]
       
    def get_passed_students(self):
        return [
            student.name
            for student in self.students
            if isinstance(student, Student) and student.has_passed(self.passing_grade)
        ]