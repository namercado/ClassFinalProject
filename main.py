from student_manager import StudentManager
from student import Student

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
