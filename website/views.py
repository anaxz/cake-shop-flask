from flask import Blueprint, render_template, request, redirect

# blueprint -> allows you sperate app out and can have the views/routes separated to multiple files
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/cakes')
def cakes():
    return render_template("cakes.html")

@views.route('/custom-order', methods=['GET', 'POST'])
def custom_order():
    if request.method == 'POST':
        cake_size = request.form.get('cake-size')
        cake_flavour = request.form.get('cake-flavour')

        print(cake_size)
        redirect('/order.html')

    return render_template("custom-order.html")

@views.route('/order')
def order():
    return render_template("order-form.html")

@views.route('/contact-us')
def contact_us():
    return render_template("contact-us.html")