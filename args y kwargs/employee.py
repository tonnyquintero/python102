class Employee:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.skills = args
        self.details = kwargs

    def show_employee(self):
        print(f'Employee: {self.name}')
        print(f'Skills: {self.skills}')
        print(f'Details: {self.details}')

employee = Employee('Anthony', 'Python', 'Java', 'C++', age=30, city='Medellin')
employee.show_employee()
        