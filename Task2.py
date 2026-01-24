"""
Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
    1.  Takes a user's first name and last name as input.
    2.  Concatenates the first name and last name into a full name.
    3.  Prints a personalized greeting message using the full name.
"""

# Function to create a personalized greeting
def personalized_greeting(first_name, last_name):
    first_name = first_name.strip().capitalize()
    last_name = last_name.strip().capitalize()
    full_name = f"{first_name} {last_name}"
    greeting_message = f"Hello, {full_name}! Welcome to the Python Program."
    return greeting_message

# Main function to take input and display greeting
def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    greeting_message = personalized_greeting(first_name, last_name)
    print(greeting_message)

if __name__ == "__main__":
    main()