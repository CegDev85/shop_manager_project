from db.run_sql import run_sql

from models.product import Product


import repositories.manufacturer_repository as manufacturer_repository 




def save(product):
    sql = "INSERT INTO products (prod_name,manufacturer_id,prod_desc,stock_qty,buy_cost,sell_price,imported) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING *"
    values = [product.prod_name, product.manufacturer.id, product.prod_desc, product.stock_qty, product.buy_cost, product.sell_price, product.imported]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product