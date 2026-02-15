"""
Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
"""

def read_file():
    try:
        with open("sample.txt", 'r') as file:                
                print("Reading file Content: ")
                # Read and print the content line by line with line numbers
                line_number = 1
                for line in file:
                    print(f"{line_number}: {line.strip()}")
                    line_number += 1

    except FileNotFoundError:
        print("Error: The file 'sample.txt' was not found.")
        
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    read_file()
