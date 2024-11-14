def divide(a: int, b: int) -> float:
    #validar que ambos parámetros sean enteros
    if not isinstance(a,int) or not isinstance(b,int):
        print('Error: Ambos parámetros deben ser enteros o flotantes')
        return None
    #Verificamos q el divisor no sea cero
    if b == 0:
        print('Error: El divisor no puede ser cero')
        return None
    
    return a/b

res_1 = divide(10, '2')
res_2 = divide(10, 0)
res_3 = divide(10, 2)
print(res_3)

#Con la finción raise

def raise_divide(a: int, b: int) -> float:
    #validar que ambos parámetros sean enteros
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError('Ambos parámetros deben ser enteros')
    #Verificamos q el divisor no sea cero
    if b == 0:
        raise ValueError('El divisor no puede ser cero')
        return None
    
    return a/b

result_1 = divide(10, '2')
result_2 = divide(10, 0)

#con try except
try: 
    res = divide(10, 2) #Error de tipo
    print(res)
except (ValueError, TypeError) as e:
    print(f'Error: {e}')