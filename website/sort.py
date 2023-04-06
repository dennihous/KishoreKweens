import sqlite3
import datetime
from Orderbook import Orderbook

class SORT:

    def __init__(self, orderbook):
        self.Orderbook = Orderbook
        self.orders = self.orderbook.orders

    def execute_trade(self):
        if not self.orders['buy', 'sell']:
            return
        
        best_bid = max(self.orders['buy'], key=lambda order: order['price'])
        best_ask = min(self.orders['sell'], key=lambda order: order['price'])

        if best_bid['price'] >= best_ask['price']:
            trade_price = best_bid['price']
            trade_quantity = min(best_bid['quantity'], best_ask['quantity'])

            best_bid['quantity'] -= trade_quantity
            best_ask['quantity'] -= trade_quantity

            if best_bid['quantity'] == 0:
                self.orders['buy'].remove(best_bid)
            if best_ask['quantity'] == 0:
                self.orders['sell'].remove(best_ask)

            trade = {
                'timestamp': datetime.datetime.now(),
                'buy_order_id': best_bid['id'],
                'sell_order_id': best_ask['id'],
                'price': trade_price,
                'quantity': trade_quantity
            }
            return trade

    '''
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
    '''
