# Exception Handling in Python

try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Invalid input! Please enter a number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Program execution completed.")