# String Handling in Python

name = "Palak Mishra"
course = "BSc IT"

# String methods
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Length:", len(name))

# Slicing
print("First 5 characters:", name[:5])

# Searching
print("Position of 'Mishra':", name.find("Mishra"))

# Formatting
print(f"Name: {name}, Course: {course}")

# Replace
print("After replacement:", name.replace("Mishra", "Student"))