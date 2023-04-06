from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import MetaData, create_engine, Table, insert, select, update, delete


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

'''
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
'''

class buy_order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    stock_name = db.Column(db.String(20))
    stock_price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer)
    date_time = db.Column(db.DateTime(timezone=True), default=func.now())

class sell_order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    stock_name = db.Column(db.String(20))
    stock_price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer)
    date_time = db.Column(db.DateTime(timezone=True), default=func.now())

'''
#define the connection details
database_uri = 'mysql+mysqlconnector://username:password@localhost:5000/database_db'

#Create an engine to connect to the database
engine = create_engine(database_uri)

#Define a metadata object to hold information about the database
metadata = MetaData()

#Define the table object
buy_order = Table('buy_order', metadata, autoload=True, autoload_with=engine)

#Create a connection to the database
with engine.connect() as connection:

    #Create a query to insert a record into the table
    data = {
        'order_id': 1,
        'user_id': 1,
        'stock_name': 'AAPL',
        'stock_price': 120.50,
        'stock_quantity': 100,
        'date_time': '2021-05-01 12:00:00'
    }

    #Create an insert query
    query = insert(buy_order).values(data)

    #Create a query to select all the records from the table
    query = select([buy_order])

    #Execute the query and fetch the results
    result_proxy = connection.execute(query)
    results = result_proxy.fetchall()

    #Print the results
    print(results)
    '''