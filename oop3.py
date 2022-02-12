# Encapsulation
from email.mime import base


class SoftwareEngineer:
    def __init__(self, name, age) -> None:
        self.name = name 
        self.age = age
        self._salary = None
        self._num_bugs_solved = 0

    def code(self):
        self._num_bugs_solved +=1
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self):
    
        return self._salary

    def _calculate_salary(self, base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value *2
        return base_value *3




se = SoftwareEngineer('Chima', 25)
print(se.name, se.age)

for i in range(70):
    se.code()

print(se._num_bugs_solved)
se.salary(6000)
print(se.salary())