# Inherits, extend, override
class Employee:
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working")

class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary ,level) -> None:
        super().__init__(name, age, salary)
        self.level = level

    def work(self):
        print(f"{self.name} is coding")

    def debug(self):
        print(f"{self.name} is debugging")

        


class Designer(Employee):
    def work(self):
        print(f"{self.name} is designing")

    def draw(self):
        print(f"{self.name} is Drawing")

# polymorphism allows us to use a class like its parent

employees = [SoftwareEngineer('max', 25, 6000, 'junior'),
            SoftwareEngineer('Lisa', 30, 9000, 'Sunior'),
            Designer('Phillip', 27, 7000)]


def motivate_employess (employees):
    for employee in employees:
        employee.work()



motivate_employess(employees=employees)


# se = SoftwareEngineer('Chima', 25, 120000, 'junior')
# se.work()
# print('\n')

# d = Designer('Phillip', 29, 7000)
# d.work()
