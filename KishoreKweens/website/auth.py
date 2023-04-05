from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Buy, Sell, Stocks

from werkzeug.security import generate_password_hash, check_password_hash
from . import db  ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)


@auth.route('/buy_order', methods=['GET', 'POST'])
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
    return render_template("buy_order.html", user=current_user, buy_orders=buy_orders)


@auth.route('/cancel_order/<int:order_id>')
@login_required
def cancel_order(order_id):
    # check if the order_id exists in the Buy table
    order = Buy.query.filter_by(id=order_id, user_id=current_user.id).first()

    # if not found in Buy table, check in Sell table
    if not order:
        order = Sell.query.filter_by(id=order_id, user_id=current_user.id).first()

    if order:
        db.session.delete(order)
        db.session.commit()
        flash('Order cancelled successfully!', category='success')
    else:
        flash('Order not found.', category='error')

    # redirect to buy or sell order page depending on the order type
    if isinstance(order, Buy):
        return redirect(url_for('auth.buy_order'))
    elif isinstance(order, Sell):
        return redirect(url_for('auth.sell_order'))


@auth.route('/sell_order', methods=['GET', 'POST'])
@login_required
def sell_order():
    if request.method == 'POST':
        user_id = current_user.id
        stock_name = request.form.get('stock_name')
        price = request.form.get('price')
        quantity = request.form.get('quantity')

        # check if the stock_name exists in the stocks table
        stock = Stocks.query.filter_by(stock_name=stock_name).first()
        if stock:
            # create a new SellOrder object with the user_id, stock_id, price, and quantity
            sell_order = Sell(user_id=user_id, stock_name=stock.stock_name, price=price, quantity=quantity)
            db.session.add(sell_order)
            db.session.commit()
            flash('Sell order successfully submitted!', category='success')
        else:
            flash('Invalid stock name. Please try again.', category='error')
    user = current_user.id
    sell_orders = Sell.query.filter_by(user_id=user).all()

    return render_template("sell_order.html", user=current_user, sell_orders=sell_orders)
