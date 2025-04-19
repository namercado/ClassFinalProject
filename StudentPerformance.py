import time

class Student:
    def __init__(self, name, student_id, score, attendance):
        self.name = name
        self.student_id = student_id
        self.score = score
        self.attendance = attendance

    def __repr__(self):
        return (f"Student(Name: {self.name}, ID: {self.student_id}, "
                f"Score: {self.score}, Attendance: {self.attendance})")


class StudentPerformanceTracker:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    # Linear Search: O(n)
    def linear_search_by_id(self, student_id):
        start = time.time()
        for student in self.students:
            if student.student_id == student_id:
                end = time.time()
                print(f"Linear search execution time: {end - start:.6f} seconds")
                return student
        end = time.time()
        print(f"Linear search execution time: {end - start:.6f} seconds")
        return None

    # Binary Search: O(log n) (requires sorted list)
    def binary_search_by_id(self, student_id):
        # First, sort the students by ID if not already sorted
        self.students.sort(key=lambda x: x.student_id)
        start = time.time()
        left, right = 0, len(self.students) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.students[mid].student_id == student_id:
                end = time.time()
                print(f"Binary search execution time: {end - start:.6f} seconds")
                return self.students[mid]
            elif self.students[mid].student_id < student_id:
                left = mid + 1
            else:
                right = mid - 1
        end = time.time()
        print(f"Binary search execution time: {end - start:.6f} seconds")
        return None

    # Sort students by score (descending): O(n log n)
    def sort_by_score(self):
        start = time.time()
        self.students.sort(key=lambda x: x.score, reverse=True)
        end = time.time()
        print(f"Sorting execution time: {end - start:.6f} seconds")

    # Display top N students: O(n)
    def display_top_students(self, n=3):
        self.sort_by_score()
        print(f"Top {n} students:")
        for student in self.students[:n]:
            print(student)

    # Calculate average score: O(n)
    def average_score(self):
        start = time.time()
        if not self.students:
            return 0
        avg = sum(student.score for student in self.students) / len(self.students)
        end = time.time()
        print(f"Average calculation execution time: {end - start:.6f} seconds")
        return avg

    # Display all students
    def display_all(self):
        for student in self.students:
            print(student)

# ----------- Example Usage ------------

tracker = StudentPerformanceTracker()
# Add sample students
tracker.add_student(Student("Alice", 101, 88, 95))
tracker.add_student(Student("Bob", 102, 92, 98))
tracker.add_student(Student("Charlie", 103, 79, 90))
tracker.add_student(Student("Diana", 104, 85, 92))
tracker.add_student(Student("Eve", 105, 95, 99))

print("\n-- All Students --")
tracker.display_all()

print("\n-- Linear Search for ID 104 --")
print(tracker.linear_search_by_id(104))

print("\n-- Binary Search for ID 104 --")
print(tracker.binary_search_by_id(104))

print("\n-- Top 3 Students --")
tracker.display_top_students(3)

print("\n-- Average Score --")
print(f"Average Score: {tracker.average_score():.2f}")

