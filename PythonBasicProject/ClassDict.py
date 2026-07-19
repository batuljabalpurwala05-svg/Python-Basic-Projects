class Employee:
    def __init__(self,emp_id,name,details):
        self.emp_id = emp_id
        self.name = name
        self.details = details
    def show_details(self):
        print("Employee ID:",self.emp_id)
        print("Employee name :",self.name)
        print("Salary:",self.details[0])
        print("Department :",self.details[1])
    
emp_dict = {}
emp_dict[101] = Employee(101, "abc", ("HR", 30000))
emp_dict[102] = Employee(102, "pqr", ("IT", 50000))
emp_dict[103] = Employee(103, "xyz", ("Finance", 45000))

for emp_id, emp_obj in emp_dict.items():
    emp_obj.show_details()