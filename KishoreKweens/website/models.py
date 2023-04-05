from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')


class Buy(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    stock_name = db.Column(db.String(10000))
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime(timezone=True), default=func.now())


class Sell(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    stock_name = db.Column(db.String(10000))
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime(timezone=True), default=func.now())


class Stocks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_name = db.Column(db.String(10000))

'''
from .models import Buy

buy_data = Buy.query.all()

buy_list = []

for data in buy_data:
    buy_dict = {
        'order_id': data.order_id,
        'stock_name': data.stock_name,
        'price': data.price,
        'quantity': data.quantity,
        'user_id': data.user_id,
        'date': data.date
    }
    buy_list.append(buy_dict)
'''
