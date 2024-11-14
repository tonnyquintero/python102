from collections import defaultdict, Counter, deque

def count_products(orders: list[str]) -> defaultdict:
    #crea un diccionario con valor por defecto de 0
    product_count = defaultdict(int)
    for product in orders:
        product_count[product] +=1
    return product_count

orders = ['laptop', 'smartphone', 'laptop', 'tablet']
count = count_products(orders)
print(count)

#contar las ventas
def count_sales(products: list[str]) -> Counter:
    #usa Counter para contar cuantos productos de cada tipo se han vendido
    return Counter(products)

sales = ['laptop', 'smartphone', 'smartphone', 'laptop', 'tablet']
result = count_sales(sales)
print(result)

def manage_delivery_queque() -> deque:
    #Crea una cola para gestionar entregas de productos
    delivery_queue = deque(['order_1', 'order_2', 'order_3'])
    delivery_queue.append('order_4') #Agrega al final de la cola
    delivery_queue.appendleft('order_0') #Agrega al principio de la cola
    delivery_queue.pop() #elimina del final
    delivery_queue.popleft() #elimina del principio
    return delivery_queue

queue = manage_delivery_queque()
print(queue)



