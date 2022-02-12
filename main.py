# position, name, age , level, salary
# se1 = ['Software engineer', 'Max', 20, 'junior', 5000]
# se2 = ['Software engineer', 'lisa', 25, 'senior', 7000]
from oop2 import Designer


d1 = ['Designer', 'phillip']


def code(se):
    print(f"{se[1]} is writing")

code(d1)

class SoftwareEngineer:
    # class attribute
    alias = "Keyboard magician"

    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    def code(self):
        print(f"{self.name} is writing code..")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}")

    # def information(self):
    #     information = f"name = {self.name}, age = {self.age}, level = {self.level} "
    #     return information

    def __str__(self) -> str:
         information = f"name = {self.name}, age = {self.age}, level = {self.level} "
         return information

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.age == other.age  

    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000

        if age < 30:
            return 7000
        return 9000




se1 = SoftwareEngineer('Max', 20, 'junior', 5000)
print(se1.name, se1.age)


se2 = SoftwareEngineer('lisa', 25, 'senior', 7000)
se3 = SoftwareEngineer('lisa', 27, 'senior', 7000)
# print(se2.alias)
print(SoftwareEngineer.alias)

se2.code_in_language('Python')
# se2.code_in_language(['c++', 'java'])


print(se1)
print(se2 == se3)

print(se2.entry_salary(24))
print(SoftwareEngineer.entry_salary(30))