def student_datbase():
    students = {}
    while True:
        print("=======MENU=======")
        print("1. Add record")
        print("2. Search record")
        print("3. Display record")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice :"))
            if choice == 1:
                rollno  = int(input("Enter roll number:"))
                name = input("Enter name:")
                age = int(input("Enter age :"))
                city = input("Enter city :")

                students.update({
                    rollno: {
                        "name": name,
                        "age": age,
                        "city": city
                    }
                })
            elif choice == 2:
                rollno = int(input("Enter the roll no data to be searched :"))
                record = students.get(rollno)
                if record:
                    print("Student Record Found")
                    print("Name:", record["name"])
                    print("Age:", record["age"])
                    print("City:", record["city"])
                else:
                    print("Student not found.")

            elif choice == 3:
                if not students:
                    print("No record available!")
                else:
                    print("All Student record")
                    for roll,data in students.items():
                        print("Roll no:",rollno,"Name:",data['name'],"Age:",data['age'],"City:",data['city'])
            
            elif choice == 4:
                print("Exiting program...")
                break
            else:
                print("Invalid choice!")

        except ValueError:
            print("Enter a valid number")
    
student_datbase()