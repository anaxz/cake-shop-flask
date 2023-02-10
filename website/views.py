from flask import Blueprint, render_template, request
from . import db
from .models import CustomOrders

# blueprint -> allows you sperate app out and can have the views/routes separated to multiple files
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/custom-order', methods=['GET', 'POST'])
def custom_order():
    if request.method == 'POST':
        size = request.form.get('cake-size')
        flavour = request.form.get('cake-flavour')
        toppings = request.form.getlist('toppings')
        fillings = request.form.getlist('fillings')
        price = request.form.get('price')

        # order = CustomOrders(customers_id='01', )

        # # add new user to db
        # db.session.add(order)
        # # update changes to db
        # db.session.commit()

        return render_template("order-complete.html", price=price)

    return render_template("custom-order.html", price='00.00')

@views.route('/order')
def order():
    return render_template("order.html")

# @views.route('/order-completed')
# def order_completed():
#     return render_template("order-complete.html", price='00.00')

@views.route('/contact-us')
def contact_us():
    return render_template("contact-us.html")