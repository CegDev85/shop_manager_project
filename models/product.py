class Products:

    def __init__(self,prod_name,prod_desc,stock_qty,buy_cost,sell_price,imported = False, id = None ):
        self.prod_name = prod_name
        self.prod_desc = prod_desc
        self.stock = stock_qty
        self.buy_cost = buy_cost
        self.sell_price = sell_price
        self.imported = imported
        self.id = id

    def mark_imported(self):
        self.imported = True