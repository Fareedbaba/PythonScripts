"""
Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
    o	Addition
    o	Subtraction
    o	Multiplication
    o	Division
3.  Displays the results of each operation on the screen.
"""

# Function to perform basic mathematical operations
def basic_math_operations(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else "Undefined (division by zero)"
    
    return addition, subtraction, multiplication, division
# Main function to take input and display results
def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    addition, subtraction, multiplication, division = basic_math_operations(num1, num2)
    print(f"Addition: {num1} + {num2} = {addition}")
    print(f"Subtraction: {num1} - {num2} = {subtraction}")
    print(f"Multiplication: {num1} * {num2} = {multiplication}")
    print(f"Division: {num1} / {num2} = {division}")

if __name__ == "__main__":
    main()