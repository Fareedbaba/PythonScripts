"""
Problem Statement: Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.
"""
final_sum = 0
for num in range(1, 51):
    final_sum += num
print(f"The sum of all integers from 1 to 50 is: {final_sum}")