class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def addAge(self, num=1):
        self.age += num
john = Person("John", 18)
john.addAge(5)
print ()