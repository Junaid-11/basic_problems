class Vehicle:
    def __init__(self, colour, name, model, wheels, brand):
        self.__colour = colour
        self.name = name
        self.model = model
        self.wheels = wheels
        self.brand = brand

    def getter(self):
        return {self.name,self.wheels,self.brand}

    def setter(self,brand):
        self.__colour=brand

class Student:
    def __init__(self,name,roll_no):
        self.__name=name
        self.roll_no=roll_no

    def display(self):
        return self.__name

    def set(self,name):
        self.__name=name


# obj=Vehicle('red','nexa',2018,'2 wheeler','tata')
# obj.setter('bmw')
# print(obj.brand)

obj=Student('tom',1)
# print(obj.display())
obj.set('tim')
# print(obj.display())
obj.__name='abc'
print(obj.display())
