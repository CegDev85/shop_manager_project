from flask import Flask, render_template, request, redirect, Blueprint
from repositories import manufacturer_repository, product_repository

from models.product import Product

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def product():
    products = product_repository.select_all()
    return render_template("products/stock.html", all_products=products)




@products_blueprint.route("/orders")
def recent_orders():
    return render_template("products/orders.html")
