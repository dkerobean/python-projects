sum = 0
def add(*args):
    for n in args:
        print(args[0])
        global sum
        sum += n
    return sum

result = add(1,3,4,5,6,6,6,6,)
print(result)

def calculate(n,**kwargs):
    for key,value in kwargs.items():
        print(key)
        print(value)

        n+=kwargs["add"]
        n+=kwargs["subtract"]
        print(f"n valeu {n}")




calculate(5,add=3,subtract=5)


class Car:

    def __init__(self,**kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="tesla", model=1920)

print(my_car.make)




