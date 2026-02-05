# Class
class Student:
    name = "sashi"


# Object
S1 = Student()
print(S1.name)


# __init__()
class Employee:
    def __init__(self, fname, salary):
        self.fname = fname
        self.salary = salary


E1 = Employee("John", "Cena")
print(E1.fname, E1.salary)


# Instance Variables (Object-Specific)
class Prod:
    def __init__(self, name):
        self.name = name


P1 = Prod("Hello World")
print(P1.name)


# Class Variable (Shared)
class Prod2:
    name = "Shirt"


print(Prod2.name)


# Instance = object = self = S1
# Instance data = Instance Variable = self.name/ self.attributes
# Instance Method (works on one object)
class Labour:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def show_details(self):
        return f"{self.name} earns {self.salary}"
    
L1 = Labour("Niraj", 100000)
print(L1.show_details())

# Class Method (Works on the class itself)
class Labour1:
    company = "TechCorp"
    
    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name
        
L2 = Labour1.change_company("HelloTech")
print(Labour1.company)

# Static Method (works like a utility tool)
# (Independent helper function inside a class. No "self", no "cls")

class Labour2:
    @staticmethod
    def calc_tax(salary):
        return salary*0.1
    
print(Labour2.calc_tax(23000))

class Math:
    @staticmethod
    def simplify(a, b, c):
        return a*c-2+b

M1 = Math    
print(Math.simplify(4, 2, 5))

class Student1:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def Add(self):
        return self.a + self.b
    
S1 = Student1(3, 5)
print(S1.Add())