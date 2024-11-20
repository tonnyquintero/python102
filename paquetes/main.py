#Importar las funciones de los modulos dentro del paquete
from ecomerce.inventory import add_product, remove_product
from ecomerce.sales import process_sale

add_product('Laptop', 10)
remove_product('Laptop')
process_sale('Laptop', 2)