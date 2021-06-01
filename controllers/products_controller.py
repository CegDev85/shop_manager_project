
from flask import Flask, render_template, request, redirect, Blueprint
from repositories import manufacturer_repository, product_repository, order_repository

from models.product import Product
from models.manufacturer import Manufacturer
from models.order import Order
import pdb;

products_blueprint = Blueprint("products", __name__)


@products_blueprint.route("/products")
def product():
    products = product_repository.select_all()
    return render_template("products/stock.html", all_products=products)

@products_blueprint.route("/product/<id>/edit", methods=["GET"])
def edit_product(id):
    product = product_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('products/edit.html', product=product, all_manufacturers=manufacturers)

@products_blueprint.route("/products/<id>", methods=["POST"])
def update_product(id):
    name = request.form['name']
    description = request.form['description']
    qty = request.form['qty']
    buy = request.form['buy']
    sell = request.form['sell']
    product = product_repository.select(id)
    product.prod_name = name
    product.prod_desc = description
    product.stock_qty = qty
    product.buy_cost = buy
    product.sell_price = sell
    # manufacturer = manufacturer_repository.select(id)
    # product = Product(name,product.manufacturer,description,qty,buy,sell,id=id)
    # print("The name is " + product.prod_name)
    product_repository.update(product)
    # product_repository.save(product)
    return redirect('/products')

@products_blueprint.route("/products/<id>/delete", methods=["POST"])
def delete_product(id):
    product_repository.delete(id)
    return redirect('/products')

@products_blueprint.route("/products/new",  methods=["GET"])
def new_product():
    products = product_repository.select_all()
    return render_template("products/new.html", all_products=products)

@products_blueprint.route("/products", methods=["POST"])
def create_product():
    name = request.form['name']
    description = request.form['description']
    qty = request.form['qty']
    buy = request.form['buy']
    sell = request.form['sell']
    # manufacturer = request.form['manufacturer']
    manufacturer_name = request.form['manufacturer']
    manufacturer = Manufacturer(manufacturer_name,"Uk")
    manufacturer = manufacturer_repository.save(manufacturer)
    # print("The id is " + manufacturer.id)
    product = Product(name,manufacturer,description,qty,buy,sell)
    product_repository.save(product)
    return redirect('/products')

# @products_blueprint.route("/products/<id>", methods=['GET'])
# def show_product(id):
#     product = product_repository.select(id)
#     stock = Product.stock_alert(id)
#     return render_template('products/show.html', product=product, stock=stock)

@products_blueprint.route("/products/<id>", methods=['GET'])
def show_product(id):
    product = product_repository.select(id)
    stock = ""
    products = product_repository.select(id)
    if products.stock_qty <= 2:
        stock = "Low Stock"
    elif products.stock_qty == 0:
        stock =  "Out of Stock"
    return render_template('products/show.html', product=product, stock=stock)


@products_blueprint.route("/new_order", methods=['GET'])
def show_order_form():
    products = product_repository.select_all()
    return render_template ('products/new_order.html', products=products) #this is how to pass it in html

@products_blueprint.route("/orders")
def orders_list():
    orders = order_repository.select_all()
    return render_template('products/orders.html', all_orders=orders)


# @products_blueprint.route("/orders", methods=['POST'])
# def new_order():
#     # print("evening" )
#     first_name = request.form['first-name']
#     last_name = request.form['last-name']
#     # print("evening" )
#     product_id = request.form['product_id'] #this is assigning the product_id to be used below
#     # product_id = int(product_id_string)
#     # pdb.set_trace()
#     product = product_repository.select(product_id)
#     qty = request.form['qty']
#     order = Order(first_name,last_name,product,qty)
#     order_repository.save(order)
#     return redirect('/orders')

@products_blueprint.route("/orders", methods=['POST'])
def new_order():
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    product_id = request.form['product_id'] #this is assigning the product_id to be used below
    product = product_repository.select(product_id)
    qty = request.form['qty']
    order = Order(first_name,last_name,product,qty)
    order_repository.save(order)
    return redirect('/orders')



