def outer_function():
    x = 'enclosing'
    def inner_function():
        nonlocal x
        x = 'modified'
        print(f'El valor en inner es: {x}')
    inner_function()
    print(f'el valor outer: {x}')
outer_function()