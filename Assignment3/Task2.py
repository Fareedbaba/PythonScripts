"""
Task 2: Using the Math Module for Calculations
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
    -   Square root of the number
    -   Natural logarithm (log base e) of the number
    -   Sine of the number (in radians)
3.   Displays the calculated results.
"""

import math
def calculate_math_functions(number):
    """This function takes a number as an argument and calculates the square root, natural logarithm, and sine of the number."""    
    sqrt_result = math.sqrt(number)
    log_result = math.log(number)
    sine_result = math.sin(number)
    return sqrt_result, log_result, sine_result
    
if __name__ == "__main__":
    # Asking the user for a number as input
    user_input = float(input("Enter a number: "))
    
    # Calculating the math functions and displaying the results
    if user_input > 0:
        results = calculate_math_functions(user_input)
        sqrt_result, log_result, sine_result = results
        print(f"Square root of {user_input}: {sqrt_result}")
        print(f"Natural logarithm of {user_input}: {log_result}")
        print(f"Sine of {user_input} (in radians): {sine_result}")
    else:
        print("Square root and logarithm are not defined for negative numbers. Please enter a positive number.")