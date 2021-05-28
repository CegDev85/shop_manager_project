from flask import Flask, render_template, request, redirect, Blueprint
from repositories import manufacturer_repository, product_repository

from models.product import Product

products_blueprint = Blueprint("products", __name__)



