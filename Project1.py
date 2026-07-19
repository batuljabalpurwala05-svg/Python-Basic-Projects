students = {}

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "B+"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def add_student():
    try:
        roll = int(input("Enter your roll number :"))
        if roll in students:
            print("Roll number already added!")
            return
        name = input("Enter your name :")

        marks = []
        print("Enter marks of 5 subjects:")
        for i in range(5):
            m = float(input("Enter your marks :"))
            marks.append(m)

        percentage = sum(marks)/5
        grade = calculate_grade(percentage)
        students[roll] = {
            "name": name,
            "marks": marks,
            "percentage": percentage,
            "grade": grade
        }
        print("Record Added Successfully!")
    
    except:
        print("Invalid input!")
def view_all():
    if not students :
        print("Record not found!")

    print("\n===== STUDENT RECORDS =====")
    for roll, data in students.items():
        print("Roll number:", roll, "| Name:", data['name'], "| Percentage:", format(data['percentage'], ".2f"), "| Grade:", data['grade'])

def search_student() :
    try:
        roll = int(input("Enter Roll No to search: "))
        
        if roll in students:
            data = students[roll]
            print("Student Record Found!")
            print("Name:",data['name'])
            print("Marks:",data['marks'])
            print("Percentage:",data['percentage'],":.2f")
            print("Grade:",data['grade'])
        else:
            print("Student Record not found!")
    
    except:
        print("Invalid input!")  

def update_student():
    try:
        roll = int(input("Enter your roll number :"))
        if roll in students:
            print("1. Update marks")
            print("2. Update name")
            choice = input("Enter your choice :")

            if choice == 1:
                students[roll]['name']= input("Enter new name :")
            elif choice == 2:
                marks= []
                print("Enter new marks:")
                for i in range(5):
                    m = float(input(f"Subject {i+1}: "))
                    marks.append(m)
                
                percentage = sum(marks) / 5
                grade = calculate_grade(percentage)

                students[roll]['marks'] = marks
                students[roll]['percentage'] = percentage
                students[roll]['grade'] = grade
            
            print("Record Updated!")
        else:
            print("Student Record not found!")
    
    except:
        print("Invalid input!")

def delete_student():
    try:
        roll = int(input("Enter roll number of the record to be deleted :"))
        if roll in students:
            del students[roll]
            print("Record deleted!!")
        else :
            print(" Student Record not found!!")
    except:
        print("Invalid input!")
    
def show_menu():
    print("====== STUDENT MANAGEMENT SYSTEM ======")
    print("1. Add Student")
    print("2. View All")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Exit")

while True:
    show_menu()

    try:
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            add_student()
        elif choice == 2:
            view_all()
        elif choice == 3:
            search_student()
        elif choice == 4:
            update_student()
        elif choice == 5:
            delete_student()
        elif choice == 6:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")
    
    except:
        print("Invalid choice !")
