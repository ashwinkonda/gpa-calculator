import database
import os

# Constants
MENU_PROMPT = """-- GPA Calculator --

Please choose one of these options:

1) About
2) Add a class
3) Add a semester
4) Calculate GPA
5) Exit

Your selection: """

GRADING_SCALE = {"A": 4.00, "A-": 3.67, "B+": 3.33, "B": 3.00, "B-": 2.67, 
                 "C+": 2.33, "C-": 2.00, "C": 2.00, "D": 1.00, "F": 0}

# Connecting to a sqlite database
connection = database.connect()

# Global variables
semester_count = database.get_semester_tables(connection)

def main():
    # Printing the Main Menu, Getting User Choice, and Validating User Choice
    while True:
        try:
            user_choice = int(input(MENU_PROMPT))
            if 1 <= user_choice <= 5:
                break
            else:
                print("Invalid choice! Try again.\n")
                continue
        except ValueError:
            print("Invalid choice! Please enter a valid number.\n")
    
    # Matching User Choice
    match user_choice:
        case 1:
            about(file_name="about.txt")
            end()
        case 2:
            add_class(semester_count)
            end()
        case 3:
            add_semester()
            end()
        case 4:
            calculate_gpa(semester_count)
            end()
        case 5:
            goodbye(semester_count)
        case _:
            pass


# All functions have a return value for testing purposes.
def about(file_name):
    try:
        # Reads the existing file
        with open(file_name, "r") as file:
            content = file.read()
            if content == "":
                print("\nThe file is empty...")
                print("All files may not have been downloaded correctly.")
                return False
            else:
                print(content)
                return True
    
    # Throws an exception if the file is not found
    except FileNotFoundError:
        print("\nFile not found...")
        print("All files may not have been downloaded.")
        return False


def add_class(semester_count):
    if not semester_count:
        print("You must add a semester before adding a class!")
        return False
    
    print(f"\nAdding to SEMESTER {semester_count} ->")

    while (name := input("Class name: ")) == "":
        print("Invalid Input! Please a enter a name.")

    while True:
        try:
            credits = int(input("Credits: "))
            if credits > 0:
                break
            else:
                print("Invalid Input! Pleae enter a postive number!")
        except (TypeError, ValueError):
            print("Invalid Input! Please enter a number!")
    
    while (grade := input("Grade Received: ")) not in GRADING_SCALE:
        print("Invalid Input! Please enter a valid letter grade.")
        print("Go to About for more information.")

    database.add_class(connection, semester_count, name, credits, grade)
    return True


def add_semester():
    global semester_count
    semester_count += 1
    database.add_semester(connection, semester_count)
    print(f"SEMESTER {semester_count} Added!")
    return semester_count


def calculate_gpa(semester_count):
    if semester_count == 0:
        print("Nothing to show...")
        return False
    
    for semester in range(1, semester_count + 1):
        print(f"\nSEMESTER {semester}:")
        semester_table = database.display_semester(connection, semester) # Getting the Semester Table
        semester_gpa = database.get_semester_gpa(connection, semester) # Getting the Semester GPA
        print(semester_table) # Printing the Semester Table
        print(f"Term GPA: {semester_gpa:.2f}") # Printing the Semester GPA
        
    cumulative_gpa = database.get_cumulative_gpa(connection, semester_count)
    print(f"\nCumulative GPA: {cumulative_gpa:.2f}")
    return True


def goodbye(semester_count):
    # There is nothing to save
    if not semester_count:
        if os.path.exists("gpa_data.db"):
            os.remove("gpa_data.db")
        print("Goodbye!")
        return False

    # Determine whether user wants to save GPA data
    while True:
        ans = input("Would you like to save your data? (y/n) ")

        if ans == "n" and os.path.exists("gpa_data.db"):
            os.remove("gpa_data.db")
            print("Goodbye!")
            break
        elif ans == "y":
            print("Saved!")
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again!")
    return True

def end():
    input("\nPress Enter to return to the main menu...")
    return main()


if __name__ == "__main__":
    main()