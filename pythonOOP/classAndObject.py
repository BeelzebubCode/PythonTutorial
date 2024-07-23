class Employee:
    salary = 2000

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

p1 = Employee("Jirat Fongda", 19)
p2 = Employee("HeHi Zeso", 50)

print(p1.name, p1.age)
print(p2.name, p2.age)
print(p1.salary, p2.salary)
p1.salary+=2000
print(p1.salary, p2.salary)
print(p1)
print(p2)