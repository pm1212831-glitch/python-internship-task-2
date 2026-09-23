# File Handling in Python

import csv
import json

# Text file - Writing
with open("sample.txt", "w") as file:
    file.write("Python Internship Task 2\n")
    file.write("File Handling Example")

# Text file - Reading
with open("sample.txt", "r") as file:
    content = file.read()

print("Text File Content:")
print(content)

# CSV file - Writing
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Roll No", "Name", "Course"])
    writer.writerow([101, "Palak", "BSc IT"])
    writer.writerow([102, "Rahul", "BCA"])

print("\nCSV file created successfully.")

# JSON file - Writing
student = {
    "roll_no": 101,
    "name": "Palak",
    "course": "BSc IT"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully.")