# Python Data Structures

# List
students = ["Palak", "Pratik", "Sneha"]
students.append("Aman")

# Tuple
courses = ("BSc IT", "BCA", "MCA")

# Set
departments = {"IT", "CS", "IT", "BCA"}

# Dictionary
student = {
    "name": "Palak",
    "roll_no": 101,
    "course": "BSc IT"
}

print("List:", students)
print("Tuple:", courses)
print("Set:", departments)
print("Dictionary:", student)

# Access dictionary value
print("Student Name:", student["name"])

# List comprehension
marks = [45, 67, 82, 39, 90]
passed = [mark for mark in marks if mark >= 40]

print("Passed Marks:", passed)