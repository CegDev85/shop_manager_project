
import pdb 
from models.product import Product
from models.manufacturer import Manufacturer
from models.order import Order


import repositories.product_repository as product_repository 
import repositories.manufacturer_repository as manufacturer_repository
import repositories.order_repository as order_repository

manufacturer_repository.delete_all()
product_repository.delete_all()
order_repository.delete_all()

manufacturer1 = Manufacturer("FunkBrands","UK")
manufacturer_repository.save(manufacturer1)

manufacturer2 = Manufacturer("PopDang", "Poland")
manufacturer_repository.save(manufacturer2)

manufacturer_repository.select_all()


product1 = Product("Pink Socks",manufacturer1,"Screaming neon socks",20,1.99,4.99)
product_repository.save(product1)

product2 = Product("Bobble Head Biden",manufacturer2,"President Biden with a fun oversized head",3,4.99,9.99,True)
product_repository.save(product2)

product3 = Product("BOOM cheddar",manufacturer2,"Exploding Cheese",100,2.49,6.99,True)
product_repository.save(product3)

product_repository.select_all()



order_repository.select_all()


pdb.set_trace()