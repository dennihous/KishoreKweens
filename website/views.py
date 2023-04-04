from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
import yfinance

from website.Orderbook import Order
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/fetch-stock-prices')
def fetch_stock_prices():
    symbols = ['AAPL', 'MSFT', 'AMZN']
    stock_prices = []

    for symbol in symbols:
        stock = yfinance.Ticker(symbol)
        todays_data = stock.history(period='1d')
        price = todays_data['Close'][0]
        stock_prices.append(price)


    return jsonify(stock_prices)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/add_order', methods=['GET', 'POST'])
@login_required
def add_order():
    if request.method == 'POST': 
        order_id = request.form.get('order_id')
        instrument = request.form.get('instrument')
        side = request.form.get('side')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        status = request.form.get('status')
        order = Order(order_id=order_id, instrument=instrument, side=side, price=price, quantity=quantity, status=status)
        db.session.add(order)
        db.session.commit()
        flash('Order added!', category='success')

    return render_template("add_orders.html", user=current_user)

'''
@views.route('/buy_order', methods=['GET', 'POST'])
@login_required
def buy_order():
    if request.method == 'POST': 
        order_id = request.form.get('order_id')
    '''    
'''
    order = json.loads(request.data)
    order_id = order['order_id']
    order = Order.query.get(order_id)
    if order:
        if order.user_id == current_user.id:
            db.session.delete(order)
            db.session.commit()

    return render_template("buy_order.html", user=current_user)
    '''