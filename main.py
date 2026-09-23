import csv
from student import Student

FILE_NAME = "student_records.csv"


def load_students():
    students = []

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = Student(
                    int(row["roll_no"]),
                    row["name"],
                    row["course"],
                    float(row["marks"])
                )
                students.append(student)

    except FileNotFoundError:
        pass

    return students


def save_students(students):
    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["roll_no", "name", "course", "marks"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for student in students:
            writer.writerow({
                "roll_no": student.roll_no,
                "name": student.name,
                "course": student.course,
                "marks": student.marks
            })


def add_student(students):
    try:
        roll_no = int(input("Enter roll number: "))

        for student in students:
            if student.roll_no == roll_no:
                print("Roll number already exists.")
                return

        name = input("Enter student name: ")
        course = input("Enter course: ")
        marks = float(input("Enter marks: "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        student = Student(roll_no, name, course, marks)
        students.append(student)
        save_students(students)

        print("Student added successfully.")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    for student in students:
        student.display()


def search_student(students):
    try:
        roll_no = int(input("Enter roll number to search: "))

        for student in students:
            if student.roll_no == roll_no:
                student.display()
                return

        print("Student not found.")

    except ValueError:
        print("Invalid roll number.")


def update_student(students):
    try:
        roll_no = int(input("Enter roll number to update: "))

        for student in students:
            if student.roll_no == roll_no:
                student.name = input("Enter new name: ")
                student.course = input("Enter new course: ")
                student.marks = float(input("Enter new marks: "))

                if student.marks < 0 or student.marks > 100:
                    print("Marks must be between 0 and 100.")
                    return

                save_students(students)
                print("Student updated successfully.")
                return

        print("Student not found.")

    except ValueError:
        print("Invalid input.")


def delete_student(students):
    try:
        roll_no = int(input("Enter roll number to delete: "))

        for student in students:
            if student.roll_no == roll_no:
                students.remove(student)
                save_students(students)
                print("Student deleted successfully.")
                return

        print("Student not found.")

    except ValueError:
        print("Invalid roll number.")


def main():
    students = load_students()

    while True:
        print("\n===== Student Record Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            print("Thank you for using Student Record Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()