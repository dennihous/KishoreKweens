from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from .models import User, Buy, Sell, Stocks

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

'''
@views.route('/buy_order', methods=['GET', 'POST'])
@login_required
def buy_order():
    if request.method == 'POST':
        user_id = current_user.id  # get the user_id from the current_user object
        stock_name = request.form.get('stock_name')
        price = request.form.get('price')
        quantity = request.form.get('quantity')

        # check if the stock_name exists in the stocks table
        stock = Stocks.query.filter_by(stock_name=stock_name).first()
        if stock:
            # create a new BuyOrder object with the user_id, stock_id, price, and quantity
            buy_order = Buy(user_id=user_id, stock_name=stock.stock_name, price=price, quantity=quantity)
            db.session.add(buy_order)
            db.session.commit()
            flash('Buy order successfully submitted!', category='success')
        else:
            flash('Invalid stock name. Please try again.', category='error')

    # Query the Buy table for all buy orders made by the current user
    user = current_user.id
    buy_orders = Buy.query.filter_by(user_id=user).all()
    return render_template("buy_order.html", user=user,  buy_orders=buy_orders)
'''