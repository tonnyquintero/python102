def check_access(func) :
    def wrapper(employee):
        #Comparar el rol 'admin'
        if employee.get('role') == 'admin' :
            return func(employee)
        else:
            print('Acceso denegado. Solo los admin pueden acceder')
    return wrapper


@check_access
def delete_employee(employee):
    print(f"El empleado {employee['name']} ha sido eliminado")

admin = {'name': 'Carlos', 'role': 'admin'}
employee = {'name': 'Ana', 'role': 'employee'}

delete_employee(admin) #OUTPUT El empleado Carlos ha sido eliminado
#delete_employee(employee) #OUTPUT Acceso denegado. Solo los admin pueden acceder