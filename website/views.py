from flask import Blueprint, render_template

# blueprint -> allows you sperate app out and can have the views/routes separated to multiple files
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/order')
def order():
    return render_template("order.html")