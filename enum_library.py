from enum import Enum

class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3

def check_order_status(status: OrderStatus):
    #comprueba el estado del pedido y devuelve el mensaje
    if status == OrderStatus.PENDING:
        return 'Order is still pending'
    elif status == OrderStatus.SHIPPED:
        return 'Order has been shipped'
    elif status == OrderStatus.DELIVERED:
        return 'order has been delivered'
    
print(OrderStatus(OrderStatus.SHIPPED))