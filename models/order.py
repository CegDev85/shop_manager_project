# import repositories.product_repository as product_repository

class Order:

    def __init__(self,first_name,last_name,product,qty,id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.product = product
        self.qty = qty
        self.id = id

    # @classmethod
    # def sell_stock(cls,id):
    #     product = product_repository.select(id)
    #     product.stock_qty -= Order.order.qty
    #     return product.stock_qty
