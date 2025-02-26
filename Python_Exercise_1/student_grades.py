#Write a Python program to create a dictionary of student names and grades, and count the number of students with grades above 90.

# Function to validate and collect student names
def get_valid_name(prompt):
    """Prompt user for a valid name containing only letters and spaces."""
    while True:
        name = input(prompt).strip()
        if not name:
            print("Name cannot be empty. Please try again.")
        elif name.replace(" ", "").isalpha():  # Allow spaces but ensure only letters
            return name
        else:
            print("Name must contain only letters and spaces. No numbers or special characters allowed.")

# Function to validate and collect grades
def get_valid_grade(name):
    """Prompt user for a valid grade between 0 and 100."""
    while True:
        try:
            grade = float(input(f"Grade for {name} (0-100): "))
            if 0 <= grade <= 100:
                return grade
            print("Grade must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Enter a numeric grade.")

# Main program
if __name__ == "__main__":
    """Collect student names and grades, then count students with grades above 90."""
    students = {}  # Dictionary to store student names and grades

    # Validate the number of students input
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            if num_students >= 0:
                break
            print("Number of students must be a non-negative integer. Please try again.")
        except ValueError:
            print("Invalid input. Enter a numeric value.")

    # Collect student names and grades
    for i in range(1, num_students + 1):
        name = get_valid_name(f"Student {i} name: ")
        grade = get_valid_grade(name)
        students[name] = grade

    # Count students with grades above 90
    count_above_90 = sum(1 for grade in students.values() if grade > 90)

    # Display results
    print("\nStudent Grades:")
    for name, grade in students.items():
        print(f"{name}: {grade}")
    print(f"Number of students with grades above 90: {count_above_90}")