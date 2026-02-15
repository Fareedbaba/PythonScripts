"""
Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

"""

def write_to_file():
    try:
        with open("output.txt", "wt") as file:
            user_input = input("Enter text to write to output.txt: ")
            file.write(user_input + "\n")
        print("Data written to output.txt successfully.")   
        # if file does not exist, a new file will be created and content will be written to the file
        # if file exists, the old content will be erased and the content will be over-written to the file
    except IOError as e:
        print(f"Error writing to file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while writing to file: {e}")

def append_to_file():
    try:
        with open("output.txt", "at") as file:
            append_input = input("Enter additional text to append to output.txt: ")
            file.write(append_input + "\n")
        print("Data appended to output.txt successfully.")    
        # if file does not exist, a new file will be created and content will be written to the file
        # if file exists, new content will be appended to the existing content on the file.
    except IOError as e:
        print(f"Error appending to file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while appending to file: {e}")

def read_file():
    try:
        with open("output.txt", "rt") as file:
            content = file.read()
            print("\nFinal content of output.txt:")
            print(content)
        print("File read successfully.")
    except FileNotFoundError:
        print("File 'output.txt' not found.")
    except IOError as e:
        print(f"Error reading file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while reading file: {e}")


if __name__ == "__main__":
    write_to_file()
    append_to_file()
    read_file() 