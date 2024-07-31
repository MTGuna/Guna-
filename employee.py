class Employee:
    'this is commom to all employees'
    empcount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empcount+=1
    def displaycount():
        print("total number of employee %d" %Employee.empcount)
    def displayEmployee(self):
        print("Name:",self.name,"salary:",self.salary)
emp1=Employee("guna",2004)
emp2=Employee("mahi",2007)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total employee:",Employee.empcount)
Employee.displaycount()

#attributes
print("Employee.__doc__:",Employee.__doc__)
print("Employee.__name__:",Employee.__name__)
print("Employee.__module__:",Employee.__module__)
print("Employee.__bases__:",Employee.__bases__)
print("Employee.__dict__:",Employee.__dict__)
