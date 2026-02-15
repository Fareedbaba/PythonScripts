"""
Task 1: Calculate Factorial Using a Function
Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
"""

# Defining the factorial function
def factorial(n):
    """This function takes a number as an argument and calculates its factorial."""
    factorial_of_number = 1
    if n == 0:
        factorial_of_number
    else:
        for i in range(1, n + 1):
            factorial_of_number *= i
    return factorial_of_number


if __name__ == "__main__":
    # Calling the function with a sample number and printing the output
    sample_number = int(input("Enter a number to calculate its factorial: "))
    if sample_number >= 0:
        factorial_of_sample_number = factorial(sample_number)
        print(f"The factorial of {sample_number} is: {factorial_of_sample_number}")
    else:
        print("Factorial is not defined for negative numbers.")
