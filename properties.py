#Las propiedades son getter, setter y deleter

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property  #aqui está implicito el getter
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError('Salary cannot be negative')
        self._salary = new_salary

    @salary.deleter
    def salary(self):
        print(f'The salary of {self.name} has been deleted')
        del self._salary

employee = Employee('Ana', 5000)
#print(employee.salary)

employee.salary = 6000
#print(employee.salary)

#del employee.salary