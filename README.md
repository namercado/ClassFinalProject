Group Project: Student Performance Tracker with Efficient Algorithms
Objective:
In this project, your team will design and implement a Python program using ObjectOriented Programming (OOP) concepts and analyze the time complexity of your code.
The program will manage student performance data and demonstrate the efficiency of
different search and sort methods.
Group Formation
• You will work in groups of 4 to 5 students.
• Your team is responsible for managing collaboration and task distribution.
• Each member must contribute to coding, documentation, and presentation.
Project Description
Your team will develop a Student Performance Tracker that:
• Uses Python classes to represent and manage student data.
• Stores each student’s name, ID, score, and attendance.
• Allow users to search, sort, and analyze student data.
• Includes both linear search (O(n)) and binary search (O(log n)) to compare
efficiency.
• Displays top-performing students and calculates the average score.
• Measures and reports actual execution time for key operations.
• Explains the time complexity of each major function in your project.
Minimum Requirements
Code Features:
1. Student class with:
o Attributes: name, student_id, score, attendance
o __repr__ method for printing
2. StudentManager class with:
o add_student() to add a new student (O(1))
o print_all_students() to display student list
o linear_search_by_name() (O(n))
o sort_students_by_score() (O(n log n)) using .sort()
o binary_search_by_score() using bisect (O(log n))
o get_top_n_students() to list top N students (O(n log n))
o average_score() to calculate class average (O(n))
3. Performance testing:
o Create 10,000 random student records
o Measure and compare time for linear vs. binary search using time.time()
Time Complexity Analysis (Required Section in Report)
Your report must:
• Include Big O notations for each key method.
• Show measured execution time for linear and binary search.
• Explain why binary search is faster, and when linear might be better.
Deliverables
Each group must submit:
1. Python Code (.py file)
2. Project Report (.pdf or .docx) that includes:
o Description of your code structure and how you used classes
o Explanation of time complexity for each function
o Screenshots of sample output
o Measured performance results
o Division of tasks among group members
3. Presentation Slides (5–7 mins per group):
o Overview of your design
o Time complexity comparison
o Key findings or lessons learned
Due Date:
Grading Criteria (Total: 100 points)
Category Points
Use of Classes & OOP Principles 20
Functional Requirements Met 20
Time Complexity Analysis 20
Performance Testing & Insight 10
Code Quality & Comments 10
Report Quality & Completeness 10
Group Presentation 10
Tips for Success
• Don’t wait until the last minute to generate performance data.
• Assign clear roles: programmer, analyst, writer, presenter.
• Use version control (GitHub or Google Drive) to manage code.
• Keep it simple and focus on clean, efficient design.
