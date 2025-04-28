# Import necessary modules
from student_manager import StudentManager  # Main management class
from student import Student  # Student data model


def main_menu():
    # Initialize the student management system
    manager = StudentManager()

    # Continuous loop for user interaction
    while True:
        # Display menu options
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

        # Get user input
        choice = input("Enter your choice (1-9): ")

        # Option 1: Add new student
        if choice == '1':
            name = input("Enter student name: ")
            try:
                # Collect and validate numerical inputs
                student_id = int(input("Enter student ID: "))
                score = int(input("Enter student score (0-100): "))
                attendance = int(input("Enter attendance percentage (0-100): "))
            except ValueError:
                print("Invalid input. Please enter numbers for ID, score, and attendance.")
                continue  # Restart loop on invalid input

            # Create and add new student
            manager.add_student(Student(name, student_id, score, attendance))
            print("Student added successfully.")

        # Option 2: Display all students
        elif choice == '2':
            manager.print_all_students()  # Uses Student's __repr__ for formatting

        # Option 3: Name search
        elif choice == '3':
            name = input("Enter name to search: ")
            student = manager.linear_search_by_name(name)
            print("Student found:", student) if student else print("Student not found.")

        # Option 4: Score sorting
        elif choice == '4':
            manager.sort_students_by_score()
            print("Students sorted by score.")

        # Option 5: Score search
        elif choice == '5':
            try:
                score = int(input("Enter score to search: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            student = manager.binary_search_by_score(score)
            print("Student found:", student) if student else print("Student with that score not found.")

        # Option 6: Top performers
        elif choice == '6':
            try:
                n = int(input("Enter N (number of top students): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            top_students = manager.get_top_n_students(n)
            print(f"Top {n} students:")
            for s in top_students:
                print(s)  # Display each top performer

        # Option 7: Class average
        elif choice == '7':
            avg = manager.average_score()
            print(f"Class average score: {avg:.2f}")  # Formatted to 2 decimal places

        # Option 8: Performance testing
        elif choice == '8':
            print("Running performance test with 10,000 students...")
            manager.performance_test()  # Includes timing comparisons

        # Option 9: Exit program
        elif choice == '9':
            print("Exiting program. Goodbye!")
            break  # Exit loop

        # Handle invalid choices
        else:
            print("Invalid choice. Please select a valid option.")


# Standard Python entry point
if __name__ == "__main__":
    main_menu()  # Start program execution
