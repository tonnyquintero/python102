def log_transaction(func):
    def wrapper():
        print('1 Log de la transaccion...')
        func()
        print('3 Log terminado.')
    return wrapper

#Para utilizar el decorador utilizamos el arroba @
@log_transaction


def procces_payment():
    print('2 Procesando pago...')

procces_payment()