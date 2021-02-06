# Defining the Employee class
class Employee:
    # Class level attributes
    totalEmployee = 0  # Count of the total no.of employees
    totalSalary = 0  # Sum of total salary of all the employees

    def __init__(self, name, family, salary, department):  # constructor
        Employee.totalEmployee += 1  # incrementing the count by 1
        Employee.totalSalary += salary  # summing up the salary
        # Initializing the instance level attributes
        self.name = name  # Public level data attribute
        self.family = family
        self.__salary = float(salary)  # Private level data attribute can be accessed inside the class only
        self.department = department

    # Function that returns the name of the employee
    def getName(self):
        return self.name

    # Function that sets the value of salary
    def getSalary(self):
        return self.__salary

    # Function that returns the value of salary
    def setSalary(self, newSalary):
        Employee.totalSalary += (newSalary - self.__salary)
        self.__salary = newSalary

    # Function that will calculate the Average salary of all the employees
    def calculateAvgSalary(self):
        return Employee.totalSalary / Employee.totalEmployee


# Defining the FulltimeEmployee subclass which inherits the properties of superclass Employee
class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department):  # Constructor
        super().__init__(name, family, salary, department)  # Calling the Employee constructor


employee1 = FulltimeEmployee("Vineeth", "Sheri", 80000, "CS")  # Created the instance of FulltimeEmployee
print("Employee1 details: ", employee1.__dict__)
employee1.setSalary(90000)  # Changing the salary of employee as we cant the change it directly because of private
print("The Employee {} new salary is: {}".format(employee1.getName(), employee1.getSalary()))

employee2 = Employee("Raj", "Krish", 60000, "CS")  # Created the instance of FulltimeEmployee
print("The Employee {} salary is: {}".format(employee2.getName(), employee2.getSalary()))
print("The Average salary of all the employees are:", employee2.calculateAvgSalary())
print("The total count of the employees is:", employee2.totalEmployee)










