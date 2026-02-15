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

def calculate_sqrt(number) :
    return math.sqrt(number)

def calculate_log(number):
    return math.log(number)

def calculate_sine(number):
    return math.sin(number)
    
if __name__ == "__main__":
    # 1. Asks the user for a number as input.
    user_input = float(input("Enter a number: "))
    
    # Calculating the math functions and displaying the results
    if user_input > 0:        
        sqrt_result = calculate_sqrt(user_input)
        log_result = calculate_log(user_input)
        sine_result = calculate_sine(user_input)
        
        print(f"Square root of {user_input}: {sqrt_result}")
        print(f"Natural logarithm of {user_input}: {log_result}")
        print(f"Sine of {user_input} (in radians): {sine_result}")
    else:
        # Handle cases where the input is not positive
        print("Please enter a positive number.")