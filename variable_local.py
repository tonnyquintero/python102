y = 100

def local_function():
    x = 10 #variable local
    print(f"El valor de la variable es {x}")

local_function()
#print(x) #Esto da error ya q la variable está en modo local

def show_global():
    print(f"El valor de la variable global es {y}")

show_global()
