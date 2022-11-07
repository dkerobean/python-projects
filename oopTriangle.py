class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_perimeter(self):
        result = self.a + self.b + self.c
        return result


triangle1 = Triangle(5,3,2)
perimeter = triangle1.calculate_perimeter()
print(perimeter)


class Person:

    def __init__(self,name):
        self.name = name


    def talk(self):
        print(f"{self.name} is talking")


p1 = Person("dickson")
talk = p1.talk()
print(talk)