#decorador que compureba si el empleado tiene un rol especifico
def check_access(required_role):
    def decorator(func):
        def wrapper(employee):
            #si el rol del empleado coincide con el rol requerido
            if employee.get('role') == required_role:
                return func(employee)
            else:
                print(f"Acceso denegado. Solo {required_role} pueden realizar esta acción")
        return wrapper
    return decorator

def log_action(func):
    def wrapper(employee):
        print(f"Registrando accion para el empleado {employee['name']}")
        return func(employee)
    return wrapper


@check_access('admin')
@log_action

def delete_employee(employee):
    print(f"El empleado {employee['name']}, ha sido eliminado")

admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}

#delete_employee(admin)
delete_employee(employee)