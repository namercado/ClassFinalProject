# Import necessary libraries
import bisect  # For binary search operations
import random  # For generating random student data
import time  # For performance timing
from tqdm import tqdm  # For progress bar visualization
from student import Student  # Import Student class from student module


class StudentManager:
    def __init__(self):
        # Initialize empty lists to store students and sorted scores
        self.students = []  # Main student database
        self.sorted_scores = []  # Cached sorted scores for binary search

    def add_student(self, student):
        # Add a student to the system
        self.students.append(student)  # Append to main list
        self.sorted_scores = []  # Reset cached scores to maintain consistency

    def print_all_students(self):
        # Display all students in the system
        if not self.students:  # Check for empty list
            print("No students in the system.")
            return
        for student in self.students:  # Iterate through all students
            print(student)  # Use Student.__repr__ for display

    def linear_search_by_name(self, name):
        # Search for student by name (case-insensitive)
        for student in self.students:  # Check each student sequentially
            if student.name.lower() == name.lower():  # Case-insensitive comparison
                return student  # Return first match
        return None  # Return None if no match found

    def sort_students_by_score(self):
        # Sort students by score and cache scores
        self.students.sort(key=lambda x: x.score)  # Sort by score attribute
        self.sorted_scores = [s.score for s in self.students]  # Cache sorted scores

    def binary_search_by_score(self, target_score):
        # Find student by score using binary search
        if not self.students:  # Empty list check
            return None
        if not self.sorted_scores:  # Ensure scores are sorted
            self.sort_students_by_score()

        # Find insertion point for target score
        index = bisect.bisect_left(self.sorted_scores, target_score)

        # Check for actual match and handle duplicates
        if index < len(self.sorted_scores) and self.sorted_scores[index] == target_score:
            # Find first occurrence in case of duplicates
            while index > 0 and self.sorted_scores[index - 1] == target_score:
                index -= 1
            return self.students[index]  # Return corresponding student
        return None

    def get_top_n_students(self, n):
        # Retrieve top N students by score
        # Sort in descending order and slice first N elements
        return sorted(self.students, key=lambda x: -x.score)[:n]

    def average_score(self):
        # Calculate average score of all students
        if not self.students:  # Handle empty list
            return 0.0
        return sum(s.score for s in self.students) / len(self.students)

    def performance_test(self):
        # Test search performance with large dataset
        names = ["John", "Jane", "Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Ethan", "Fiona", "George", "Hannah", "Ian", "Julia",
                 'Kevin', "Laura", "Michael", "Nina", "Oliver", "Paula", "Quentin", "Rachel", "Steven", "Tina"]
        self.students = []  # Reset student list

        # Generate 10,000 random students with progress bar
        for _ in tqdm(range(10000), desc="Creating students"):
            student = Student(
                name=random.choice(names) + " " + random.choice(["Smith", "Lee", "Doe","Anderson", "Brown", "Clark", "Davis", "Evans",
    "Garcia", "Harris", "Johnson", "King", "Lewis",
    "Martinez", "Nelson", "Parker", "Roberts", "Scott",
    "Turner", "Walker", "Young", "Zimmerman", "Lopez"]),
                student_id=random.randint(1000, 9999),
                score=random.randint(0, 100),
                attendance=random.randint(50, 100)
            )
            self.add_student(student)

        # Add test student with known values
        test_student = Student("John Doe", 9999, 85, 90)
        self.add_student(test_student)

        # Test linear search performance
        start = time.time()
        found_linear = self.linear_search_by_name("John Doe")
        linear_time = time.time() - start

        # Test binary search performance (requires sorted data)
        self.sort_students_by_score()
        start = time.time()
        found_binary = self.binary_search_by_score(85)
        binary_time = time.time() - start

        # Print results
        print(f"Linear search time: {linear_time:.6f}s")
        print(f"Binary search time: {binary_time:.6f}s")
        print(f"Found with linear: {found_linear}")
        print(f"Found with binary: {found_binary}\n")
