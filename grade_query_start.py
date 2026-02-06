##
#
# Manage student grades.
# Creates dictionary
grades = {}

while True:
    # This takes all inputs regardless of case
    choice = input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? ").upper()
    # Adds new student
    if choice == 'A':
        name = input("Enter the name of the student: ")

        if name in grades:
            print("Sorry, that student is already present.")
        else:
            grade_input = input("Enter the student's grade: ")
            try:
                grade = int(grade_input)
                if 0 <= grade <= 100:
                    grades[name] = grade
                else:
                    print("Please enter grade as number 0-100")
            except ValueError:
                print("Please enter grade as number 0-100")

    # Remove student
    elif choice == 'R':
        name = input("What student do you want to remove? ")
        if name in grades:
            grades.pop(name)
        else:
            print("Sorry, that student doesn't exist and couldn't be removed.")

    # Changes student grade
    elif choice == 'M':
        name = input("Enter the name of the student to modify: ")
        if name in grades:
            print("The old grade is", grades[name])
            grade_input = input("Enter the new grade: ")
            try:
                grade = int(grade_input)
                if 0 <= grade <= 100:
                    grades[name] = grade
                else:
                    print("Please enter grade as number 0-100")
            except ValueError:
                print("Please enter grade as number 0-100")

    # Prints grade average and th students and scores stored in the dictionary
    elif choice == 'P':
        if grades:
            average = sum(grades.values()) / len(grades)
            print("The average grade is", average)
            for student, grade in grades.items():
                print(student, ":", grade)
        else:
            print("No students to display.")
    # Quits
    elif choice == 'Q':
        print("Goodbye!")
        break

    # Handle invalid input
    else:
        print("Sorry, that wasn't a valid choice.")


 
