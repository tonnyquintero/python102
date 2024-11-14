#IDs de los empleados
id1: int = 101
id2: int = 102

total_id: int = id1 + id2

print(total_id)

#anotaciones en funciones (las anotaciones son estilo typescript)
def add_employee_ids(idd1: int, idd2: int) -> int:
    return idd1+idd2

print(add_employee_ids(201,202))

#anotaciones en clases (poo)
class Employee:
    name: str
    age: int
    salary: float

    def __init__(self, name: str, age: int, salary:float):
        self.name = name
        self.age = age
        self.salary = salary

    def introduce(self) -> str :
        return f"Hola me llamo {self.name} y tengo {self.age} años"
    
employee1 = Employee('Carlos', 30, 3500.00)
print(employee1.introduce())