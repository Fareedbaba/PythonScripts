"""
Task 1: Calculate Factorial Using a Function
Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
"""
from math import factorial

def factorial_using_loop(n):
    """This function takes a number as an argument and calculates its factorial."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def factorial_using_recursion(n):
    """This function takes a number as an argument and calculates its factorial using recursion."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_using_recursion(n - 1)

def factorial_using_builtin(n):
    """This function takes a number as an argument and calculates its factorial using the built-in math.factorial function."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    else:
        return factorial(n)

if __name__ == "__main__":
    # Calling the function with a sample number and printing the output
    sample_number = 5
    print(f"The factorial of {sample_number} is: {factorial_using_loop(sample_number)}")
    print(f"The factorial of {sample_number} is: {factorial_using_recursion(sample_number)}")
    print(f"The factorial of {sample_number} is: {factorial_using_builtin(sample_number)}")