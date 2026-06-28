def manage_marks():
    marks = []

    # Input marks
    for i in range(5):
        try:
            m = float(input(f"Enter marks {i+1}: "))
            marks.append(m)
        except ValueError:
            print("Please enter a valid number.")
            return

    # Calculations (AFTER loop)
    average = sum(marks) / len(marks)
    maximum = max(marks)
    minimum = min(marks)

    # Sort in descending order
    marks.sort(reverse=True)

    # Output
    print("\nMarks in descending order:", marks)
    print("Student result:")
    print("Average:", average)
    print("Maximum marks:", maximum)
    print("Minimum marks:", minimum)


# Call function
manage_marks()