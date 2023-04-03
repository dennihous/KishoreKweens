import sqlite3

class SORT:
    def __init__(self):
        self.exchanges = []
        self.order_books = {}

    def add_exchange(self, exchange):
        self.exchanges.append(exchange)

    def execute_trade(self, instrument, quantity, price, side, username):
        #Get all the orderbooks for the given instrument
        
        
        # Match orders to execute trades
        # Update order status and trade history
        pass
