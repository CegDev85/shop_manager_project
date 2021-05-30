from flask import Flask, render_template, request, redirect, Blueprint
from repositories import manufacturer_repository, product_repository

from models.product import Product

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
    # manufacturer_id = request.form['manufacturer']
    manufacturer = manufacturer_repository.select(id)
    product = Product(name,manufacturer,description,qty,buy,sell)
    product_repository.update(product)
    return redirect('/products')

@products_blueprint.route("/products/<id>/delete", methods=["POST"])
def delete_product(id):
    product_repository.delete(id)
    return redirect('/products')


@products_blueprint.route("/orders")
def recent_orders():
    return render_template("products/orders.html")
