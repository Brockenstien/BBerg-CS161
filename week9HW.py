# PROBLEM 1
print("---Problem 1---")

# Make a class Students that contains the name, age, and grade of the student
class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # Print out the name, age, and grade of the given student on separate lines
    def info(self):
        return f'Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}'

# Define two separate students
stud1 = Students("Bobby", "12", "7th")
stud2 = Students("Sharl", "15", "10th")

# Get their info
print(stud1.info())
print(stud2.info())


# PROBLEM 2
print("\n---Problem 2---")

# Make a class Staff that contains the name, department, role, and salary of the staff member
class Staff:
    def __init__(self, name, department, role, salary):
        self.name = name
        self.department = department
        self.role = role
        self.salary = salary

# Make a child class of Staff called Teacher that additionally contains the age of the staff member
class Teacher(Staff):
    def __init__(self, name, department, role, salary, age):
        super().__init__(name, department, role, salary)
        self.age = age

    # Print out the name, age, role, and department of the given teacher on separate lines
    def info(self):
        return f'Name: {self.name}\nAge: {self.age}\nRole: {self.role}\nDepartment: {self.department}'

# Define two separate teachers
teach1 = Teacher("Sean", "Science", "Teacher", 50000, 30)
teach2 = Teacher("Tacky", "English", "Teacher", 50000, 58)

# Get their info
print(teach1.info())
print(teach2.info())



# PROBLEM 3
print("\n---Problem 3---")

# Define a class Square with 1 attribute
class Square:
    def __init__(self, sideLen):
        self.sideLen = sideLen

    # Define a method to get the area of the square
    def area(self):
        return f'Area = {str(self.sideLen ** 2)}cm'

    # Define a method to get the perimeter of the square
    def perimeter(self):
        return f'Perimeter = {str(self.sideLen * 4)}cm'

square1 = Square(4)
square2 = Square(10)
square3 = Square(1)


print(f'Square 1: {square1.area()} | {square1.perimeter()}')
print(f'Square 2: {square2.area()} | {square2.perimeter()}')
print(f'Square 3: {square3.area()} | {square3.perimeter()}')

