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

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        product = Product(result['prod_name'], manufacturer, result['prod_desc'], result['stock_qty'], result['buy_cost'], result['sell_price'], result['imported'], result['id'] )
    return product

def select_all():
    products =[]
    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        product = Product(row['prod_name'], manufacturer, row['prod_desc'], row['stock_qty'], row['buy_cost'], row['sell_price'], row['imported'], row['id'])
        products.append(product)
    return products


def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def update(product):
    sql = "UPDATE products SET (prod_name, manufacturer_id, prod_desc, stock_qty, buy_cost, sell_price, imported) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.prod_name, product.manufacturer.id, product.prod_desc, product.stock_qty, product.buy_cost, product.sell_price, product.imported, product.id]
    run_sql(sql, values)