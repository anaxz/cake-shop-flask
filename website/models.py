from . import db  #import from __init__
from sqlalchemy.sql import func

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(150), nullable=False)
    surname = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    address = db.Column(db.String(280))

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False)
    image = db.Column(db.String(300), nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customers_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    #default=func.now() -> stores the current date time
    dateOrdered = db.Column(db.DateTime(timezone=True), default=func.now())
    deliveryDate = db.Column(db.DateTime)
    cakeSize = db.Column(db.String(10), nullable=False)
    cakeFlavour = db.Column(db.String(25), nullable=False)

class CustomOrders(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customers_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    dateOrdered = db.Column(db.DateTime(timezone=True), default=func.now())
    deliveryDate = db.Coulmn(db.DateTime, nullable=False)
    cakeSize = db.Column(db.String(10), nullable=False)
    cakeFlavour = db.Column(db.String(25), nullable=False)
    cakeToppings = db.Column(db.String(25), nullable=False)
    cakeFillings = db.Column(db.String(25), nullable=False)

class CustomerOrders(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    orders_id = db.Column(db.Integer, db.ForeignKey('orders.id'))

class Enquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(150), nullable=False)
    surname = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    content =  db.Column(db.String(1000), nullable=False)
