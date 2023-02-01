from flask import Blueprint, render_template, request

products = Blueprint('products', __name__)

@products.route('/cakes')
def cakes():
    if request.method == 'POST':
        pass

    return render_template("cakes.html")

