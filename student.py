class Student:
    def __init__(self, roll_no, name, course, marks):
        self.roll_no = roll_no
        self.name = name
        self.course = course
        self.marks = marks

    def display(self):
        print(
            f"Roll No: {self.roll_no}, "
            f"Name: {self.name}, "
            f"Course: {self.course}, "
            f"Marks: {self.marks}"
        )