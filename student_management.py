import re
import logging


class Student:
    def __init__(self, student_id, name, contact, subjects):
        self.student_id = student_id
        self.name = name
        self.contact = contact
        self.subjects = subjects  # Dictionary of subjects with marks and fees

    def display_student(self):
        print(f"student_id: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Contact Number: {self.contact}")
        for subject, details in self.subjects.items():
            print(f"Subject: {subject}, Marks: {details['marks']}, Fees: {details['fees']}")
        print()


class StudentManagement:
    def __init__(self):
        self.students = {}  # Dictionary to hold student data

    def add_student(self):
        try:
            student_id = input("Enter Student ID: ")
            if student_id in self.students:
                print("Student ID already exists.")
                return

            name = input("Enter Student Name: ")
            while not name.isalpha():
                print("Invalid name. Only letters are allowed.")
                name = input("Enter Student Name again: ")

            contact = input("Enter Contact Number: ")
            while not (contact.isdigit() and len(contact) == 10):
                print("Invalid contact number. Enter a 10-digit number.")
                contact = input("Enter Contact Number again: ")

            subjects = {}
            while True:
                subject = input("Enter a Subject: ")
                marks = int(input("Enter Marks: "))
                fees = int(input("Enter Fees: "))
                subjects[subject] = {'marks': marks, 'fees': fees}

                another = input("Add another subject? (yes/no): ").lower()
                if another != 'yes':
                    break

            self.students[student_id] = Student(student_id, name, contact, subjects)
            print("Student added successfully!\n")
            logging.info(f"Added student with ID: {student_id}")

        except Exception as e:
            print("An error occurred:", e)

    def remove_student(self):
        student_id = input("Enter Student ID to remove: ")
        if student_id in self.students:
            confirm = input("Are you sure you want to delete this student? (Y/N): ")
            if confirm.lower() == 'y':
                del self.students[student_id]
                print("Student removed successfully.")
                logging.info(f"Removed student with ID: {student_id}")
        else:
            print("Student ID not found.")

    # def view_all_students(self):
    #     if not self.students:
    #         print("No students in the system.")
    #     else:
    #         for student_id, details in self.students.items():
    #             print(f"ID: {student_id}, Name: {details.name}, Contact: {details.contact}")

    def view_student(self):
        student_id = int(input("Enter the student_id  of the student to view: "))
        if student_id in self.students:
            self.students[student_id].display_student()
        else:
            print("Student not found.")

    def add_marks(self):
        student_id = input("Enter Student ID to add marks: ")
        if student_id in self.students:
            try:
                marks = float(input("Enter marks for the student: "))
                if marks < 0 or marks > 100:
                    print("Invalid marks. Please enter a value between 0 and 100.")
                    return
                self.students[student_id]['marks'] = marks
                print("Marks added successfully.")
                logging.info(f"Added marks for student ID: {student_id}")
            except ValueError:
                print("Invalid input. Please enter a numeric value for marks.")
        else:
            print("Student ID not found.")

    def view_all_students(self):
        if not self.students:
            print("No students in the system.")
        else:
            for student_id, details in self.students.items():
                marks = details.get('marks', 'N/A')  # Display 'N/A' if marks are not assigned
                print(f"ID: {student_id}, Name: {details.name}, Contact: {details.contact}, Marks: {marks}")

    def view_student_details(self):
        student_id = input("Enter your Student ID to view details: ")
        if student_id in self.students:
            details = self.students[student_id]
            print(f"ID: {student_id}, Name: {details['name']}, Contact: {details['contact']}")
        else:
            print("Student ID not found.")

    def view_student_marks(self):
        student_id = input("Enter your Student ID to view marks: ")
        if student_id in self.students:
            details = self.students[student_id]
            marks = details.get('marks', 'No marks available')
            print(f"ID: {student_id}, Name: {details['name']}, Marks: {marks}")
        else:
            print("Student ID not found.")