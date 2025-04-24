import bisect
import random
import time
from tqdm import tqdm
from student import Student

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
        names = ["John", "Jane", "Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
        self.students = []
        for _ in tqdm(range(10000), desc="Creating students"):
            student = Student(
                name=random.choice(names) + " " + random.choice(["Smith", "Lee", "Doe"]),
                student_id=random.randint(1000, 9999),
                score=random.randint(0, 100),
                attendance=random.randint(50, 100)
            )
            self.add_student(student)

        test_student = Student("Z_TEST_NAME", 9999, 85, 90)
        self.add_student(test_student)

        start = time.time()
        found_linear = self.linear_search_by_name("Z_TEST_NAME")
        linear_time = time.time() - start

        self.sort_students_by_score()
        start = time.time()
        found_binary = self.binary_search_by_score(85)
        binary_time = time.time() - start

        print(f"Linear search time: {linear_time:.6f}s")
        print(f"Binary search time: {binary_time:.6f}s")
        print(f"Found with linear: {found_linear}")
        print(f"Found with binary: {found_binary}\n")
