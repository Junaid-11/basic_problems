class Student:
    def __init__(self,name:int,age:int):        # self is a reference to the current instance of the class, and is used to access variables that belongs to the class.
        self._name=name
        self.age=age

    def getter(self):
        return self._name

    def setter(self,name):
        self._name=name


obj=Student('junaid',21)
obj.setter('javed')
print(obj._name)
# print(obj.name)
# obj.setter('javed')
# print(obj.getter())
# print(obj.name)

