import asyncio 

async def process_data(data):
    print(f'Procesando {data}...')
    #simular una operacion
    await asyncio.sleep(5)
    print(f'{data} procesado.')
    return data * 2

async def main():
    print('Inicio de procesamiento')
    result = await process_data('archivo.txt')
    print(f'Resultado: {result}')

asyncio.run(main())