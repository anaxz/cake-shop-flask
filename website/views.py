from flask import Blueprint, render_template

# blueprint -> allows you sperate app out and can have the views/routes separated to multiple files
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/cakes')
def cakes():
    return render_template("cakes.html")

@views.route('/custom-order')
def custom_order():
    return render_template("custom-order.html")

@views.route('/contact-us')
def contact_us():
    return render_template("contact-us.html")

@views.route('/login')
def login():
    return render_template("login.html")