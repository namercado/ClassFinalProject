import bisect
import random
import time

class Student:
    def __init__(self, name, student_id, score, attendance):
        self.name = name
        self.student_id = student_id
        self.score = score
        self.attendance = attendance

    def __repr__(self):
        return (f"Student(name={self.name!r}, id={self.student_id}, "
                f"score={self.score}, attendance={self.attendance}%)")

class StudentManager:
    def __init__(self):
        self.students = []
        self.sorted_scores = []

    def add_student(self, student):
        self.students.append(student)

    def print_all_students(self):
        if not self.students:
            print("No students in the system.")
            return
        for student in self.students:
            print(student)

    def linear_search_by_name(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    def sort_students_by_score(self):
        self.students.sort(key=lambda x: x.score)
        self.sorted_scores = [s.score for s in self.students]

    def binary_search_by_score(self, target_score):
        if not self.students:
            return None
        if not self.sorted_scores:
            self.sort_students_by_score()
        index = bisect.bisect_left(self.sorted_scores, target_score)
        if index < len(self.sorted_scores) and self.sorted_scores[index] == target_score:
            while index > 0 and self.sorted_scores[index-1] == target_score:
                index -= 1
            return self.students[index]
        return None

    def get_top_n_students(self, n):
        return sorted(self.students, key=lambda x: -x.score)[:n]

    def average_score(self):
        if not self.students:
            return 0.0
        return sum(s.score for s in self.students) / len(self.students)

    def performance_test(self):
        # Generate 10,000 random students
        names = ["John", "Jane", "Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
        self.students = []
        for _ in range(10000):
            student = Student(
                name=random.choice(names) + " " + random.choice(["Smith", "Lee", "Doe"]),
                student_id=random.randint(1000, 9999),
                score=random.randint(0, 100),
                attendance=random.randint(50, 100)
            )
            self.add_student(student)

        # Add test student for reliable searches
        test_student = Student("Z_TEST_NAME", 9999, 85, 90)
        self.add_student(test_student)

        # Linear search timing
        start = time.time()
        found_linear = self.linear_search_by_name("Z_TEST_NAME")
        linear_time = time.time() - start

        # Binary search preparation and timing
        self.sort_students_by_score()
        start = time.time()
        found_binary = self.binary_search_by_score(85)
        binary_time = time.time() - start

        print(f"Linear search time: {linear_time:.6f}s")
        print(f"Binary search time: {binary_time:.6f}s")
        print(f"Found with linear: {found_linear}")
        print(f"Found with binary: {found_binary}\n")

def main_menu():
    manager = StudentManager()
    while True:
        print("\n--- Student Performance Tracker Menu ---")
        print("1. Add a student")
        print("2. Display all students")
        print("3. Linear search by name")
        print("4. Sort students by score")
        print("5. Binary search by score")
        print("6. Display top N students")
        print("7. Calculate average score")
        print("8. Performance test (10,000 students)")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            name = input("Enter student name: ")
            try:
                student_id = int(input("Enter student ID: "))
                score = int(input("Enter student score (0-100): "))
                attendance = int(input("Enter attendance percentage (0-100): "))
            except ValueError:
                print("Invalid input. Please enter numbers for ID, score, and attendance.")
                continue
            manager.add_student(Student(name, student_id, score, attendance))
            print("Student added successfully.")

        elif choice == '2':
            manager.print_all_students()

        elif choice == '3':
            name = input("Enter name to search: ")
            student = manager.linear_search_by_name(name)
            if student:
                print("Student found:", student)
            else:
                print("Student not found.")

        elif choice == '4':
            manager.sort_students_by_score()
            print("Students sorted by score.")

        elif choice == '5':
            try:
                score = int(input("Enter score to search: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            student = manager.binary_search_by_score(score)
            if student:
                print("Student found:", student)
            else:
                print("Student with that score not found.")

        elif choice == '6':
            try:
                n = int(input("Enter N (number of top students): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            top_students = manager.get_top_n_students(n)
            print(f"Top {n} students:")
            for s in top_students:
                print(s)

        elif choice == '7':
            avg = manager.average_score()
            print(f"Class average score: {avg:.2f}")

        elif choice == '8':
            print("Running performance test with 10,000 students...")
            manager.performance_test()

        elif choice == '9':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
