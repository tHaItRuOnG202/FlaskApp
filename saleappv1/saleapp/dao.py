import json
from saleapp import app, db
from saleapp.models import Category


def load_categories():
    return Category.query.all()


def load_products(cate_id=None):
    query = Product.query

    if cate_id:
        query = query.filter(Product.category_id.__eq__(cate_id))

    return query.all()
