from student_management import StudentManagement
import logging

# Configure logging
logging.basicConfig(filename='system_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(message)s')


def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Counsellor Menu")
        print("2. Faculty Menu")
        print("3. Student Menu")
        print("4. Exit")

        choice = input("Enter your choice:")

        if choice == '1':
            counsellor_menu()
        elif choice == '2':
            faculty_menu()
        elif choice == '3':
            student_menu()  # Call the student menu
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


def counsellor_menu():
    sm = StudentManagement()
    while True:
        print("1. Add Student")
        print("2. Remove Student")
        print("3. View All Students")
        print("4. View Specific Student")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            sm.add_student()
        elif choice == '2':
            sm.remove_student()
        elif choice == '3':
            sm.view_all_students()
        elif choice == '4':
            sm.view_student()
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


def faculty_menu():
    sm = StudentManagement()
    while True:
        print("\nFaculty Operations:")
        print("1. Add Marks to Student")
        print("2. View All Students")
        print("3. Go Back To Main Menu")

        choice = input("Enter a choice by Faculty: ")

        if choice == '1':
            sm.add_marks()
        elif choice == '2':
            sm.view_all_students()
        else:
            print("Invalid option. Returning to main menu.")
            break


def student_menu():
    sm = StudentManagement()
    while True:
        print("\nStudent Operations:")
        print("1. View My Details")
        print("2. View My Marks")
        print("3. Back to Main Menu")

        choice = input("Enter a choice by Student: ")

        if choice == '1':
            sm.view_student_details()
        elif choice == '2':
            sm.view_student_marks()
        elif choice == '3':
            print("Returning to main menu.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main_menu()

