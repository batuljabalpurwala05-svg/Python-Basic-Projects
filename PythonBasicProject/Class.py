class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.marks_list = []

    def add_marks(self,m):
        try:
            m = float(m)
            if m <0 or m>100:
                raise ValueError("Marks should be between 0 to 100")
            
            self.marks_list.append(m)

        except ValueError:
            print("Invalid marks")
    
    def average_marks(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)
    
    def display_info(self):
        print("--- Student Details ---")
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        print("Marks:", self.marks_list)
        print("Average:", self.average_marks())
    
try :
        name = input("Enter student name: ")
        rollno = int(input("Enter roll number: "))
        
        s1 = Student(name,rollno)
        for i in range(5):
            mark = input("Enter marks :")
            s1.add_marks(mark)


        s1.display_info()
except:
    print("Something went wrong!")