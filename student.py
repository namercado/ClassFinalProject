# Define a class named 'Student' to represent a student's information
class Student:
    # The constructor (__init__) initializes a new Student object with the provided attributes
    def __init__(self, name, student_id, score, attendance):
        self.name = name                # Store the student's name
        self.student_id = student_id    # Store the student's unique ID
        self.score = score              # Store the student's score (e.g., grade or marks)
        self.attendance = attendance    # Store the student's attendance percentage

    # The __repr__ method defines how to represent the Student object as a string
    def __repr__(self):
        # Return a formatted string that shows all the student's details
        return (f"Student(name={self.name!r}, id={self.student_id}, "
                f"score={self.score}, attendance={self.attendance}%)")
