#Write a program to create a child class Teacher that will inherit the properties of Parent class Staff

class Staff:

    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Role:", self.role)
        print("Department:", self.dept)
        print("Salary:", self.salary)




class Teacher(Staff):

    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Teacher","English",5000)


teacher = Teacher("Lia",33)
teacher.show_details()


#Python OOPs Exercise 6: Create a class Teacher with name, age, and salary attributes, where salary must be a private
# attribute that cannot be accessed outside the class.

class Teacher():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        # private variable
        self.__salary = salary

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        #access private attribute inside the class
        print("Salary: ", self.__salary)

teacher = Teacher("Raj", 45, 25000)

teacher.show_details()

#Write a Python class Square, and define two methods that return the square area and perimeter.

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4*(self.side)

#initialize the objects of Square class
square1 = Square(10)
square2 = Square(20)

print("The Area of square1 is:", square1.area())
print("The Perimeter of square1 is:", square1.perimeter())

print("\n\nThe Area of square2 is:", square2.area())
print("The Perimeter of square2 is:", square2.perimeter())



