#Student = st


class Student:
    def __init__(self, st_id, name, grade, attendancePercent):
        self.st_id = st_id
        self.name = name
        self.grade = grade
        self.attendancePercent = attendancePercent

    def __repr__(self):
        return f"Student(ID: {self.st_id}, Name: {self.name}, Grade: {self.grade}, Attendance %: {self.attendancePercent})"


class GradeTracker:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def linear_search_by_id(self, st_id):
        for student in self.students:
            if student.st_id == st_id:
                return student
        return None

    def binary_search_by_id(self, st_id):
        self.students.sort(key=lambda st: st.st_id)
        left, right = 0, len(self.students) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.students[mid].st_id == st_id:
                return self.students[mid]
            elif self.students[mid].st_id < st_id:
                left = mid + 1
            else:
                right = mid - 1
        return None

    def sort_by_grade(self):
        self.students.sort(key=lambda st: st.grade, reverse=True)

    def analyze_grade(self):
        if not self.students:
            return "No students to analyze."

        average_grade = sum(st.grade for st in self.students) / len(self.students)
        highest_grade = max(st.grade for st in self.students)
        lowest_grade = min(st.grade for st in self.students)

        return {
            "average_grade": average_grade,
            "highest_grade": highest_grade,
            "lowest_grade": lowest_grade
        }


tracker = GradeTracker()

tracker.add_student(Student(1, "Alice Smith", 94, 95, ))
tracker.add_student(Student(2, "Bob Johnson", 83, 80))
tracker.add_student(Student(3, "Charlie Davis", 75, 100))
tracker.add_student(Student(4, "David Miller", 92, 70))

print("Linear Search for ID 3:", tracker.linear_search_by_id(3))
print("Binary Search for ID 2:", tracker.binary_search_by_id(2))

tracker.sort_by_grade()
print("Students sorted by grade:")
for st in tracker.students:
    print(st)

analysis = tracker.analyze_grade()
print("Grade Analysis:", analysis)
