class Student:
    def __init__(self, name, student_id, score, attendance):
        self.name = name
        self.student_id = student_id
        self.score = score
        self.attendance = attendance

    def __repr__(self):
        return (f"Student(name={self.name!r}, id={self.student_id}, "
                f"score={self.score}, attendance={self.attendance}%)")