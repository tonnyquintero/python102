#Se aplica para infinidad de parametros que la función desee incorporar
def print_info(**kwargs) :
    for key, value in kwargs.items():
        print(f'{key}: {value}')



print_info(name='Carlos', age=30, student=False, money=4500)