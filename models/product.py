# import repositories.product_repository as product_repository
import pdb;

class Product:

    def __init__(self,prod_name,manufacturer,prod_desc,stock_qty,buy_cost,sell_price,imported = False, id = None ):
        self.prod_name = prod_name
        self.manufacturer = manufacturer
        self.prod_desc = prod_desc
        self.stock_qty = stock_qty
        self.buy_cost = buy_cost
        self.sell_price = sell_price
        self.imported = imported
        self.id = id

    def mark_imported(self):
        self.imported = True

    # @classmethod
    # def stock_alert(cls,id):
    #     product = product_repository.select(id)
    #     if product.stock_qty <= 2:
    #         return "Low Stock"
    #     elif product.stock_qty == 0:
    #         return "Out of Stock"