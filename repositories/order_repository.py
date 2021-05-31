# from controllers.products_controller import product
from db.run_sql import run_sql

from models.order import Order
import pdb

import repositories.product_repository as product_repository


def save(order):
    sql = "INSERT INTO orders (first_name, last_name, product_id,qty) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [order.first_name, order.last_name, order.product.id, order.qty]
    results = run_sql(sql, values)
    id = results[0]['id']
    order.id = id
    return order

def select_all():
    orders = []
    sql = "SELECT * FROM orders"
    results = run_sql(sql)

    for row in results:
        product = product_repository.select(row['product_id'])
        order = Order(row['first_name'], row['last_name'], product, row['qty'], row['id'])
        orders.append(order)
    return orders

def select(id):
    order = None
    sql = "SELECT * FROM orders WHERE id = %s"
    values = [id]
    result = run_sql(sql ,values)[0]

    if result is not None:
        product = product_repository.select(result['product_id'])
        order = Order(result['first_name'],result['last_name'], product, result['qty'], result['id'] )
    return order

def delete(id):
    sql = "DELETE FROM orders WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM orders"
    run_sql(sql)

def update(order):
    sql = "UPDATE orders SET (first_name, last_name, product_id, qty) = (%s, %s, %s, %s) WHERE id = %s"
    values = [order.first_name, order.last_name, order.product.id, order.id]
    run_sql(sql, values)