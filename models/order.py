class Order:

    def __init__(self,first_name,last_name,product,qty,id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.product = product
        self.qty = qty
        self.id = id


    def sell_stock(product,qty):
        product.stock_qty -= qty
        return product.stock_qty
