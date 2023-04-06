import sqlite3


class Orderbook:
    
    def __init__(self):
        self.orders = self.load_orders()

    def load_orders(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM buy_order")
        buy_rows = c.fetchall()
        c.execute("SELECT * FROM sell_order")
        sell_rows = c.fetchall()
        conn.close()

        orders = {'buy': [], 'sell': []}
        for row in buy_rows:
            order_id, user_id, stock_name, stock_price, stock_quantity, date_time = row
            order = {'order_id': order_id, 'user_id': user_id, 'stock_name': stock_name, 'stock_price': stock_price, 'stock_quantity': stock_quantity, 'date_time': date_time}
            orders['buy'].append(order)

        for row in sell_rows:
            order_id, user_id, stock_name, stock_price, stock_quantity, date_time = row
            order = {'order_id': order_id, 'user_id': user_id, 'stock_name': stock_name, 'stock_price': stock_price, 'stock_quantity': stock_quantity, 'date_time': date_time}
            orders['sell'].append(order)

        return orders
    
    def get_orders(self):
        return self.orders

        
        '''   
        self.orders = {'buy': [], 'sell': []}
    '''
    

    '''
    def new_order(self, order):
        side = order[side]
        self.orders[side].append(order)
    '''
'''
    def cancel_order(self, order_id):
        for side in ['buy', 'sell']:
            for order in self.orders[side]:
                if order.id == order_id:
                    self.orders[side].remove(order)
                    
'''
'''
    def get_order_status(self, order_id):
        for order in self.orders:
            if order.id == order_id:
                return order.status
'''

class Order:
    # Status refers to partially filled or fully filled
    def __init__(self, order_id, instrument, side, price, quantity, status):
        self.order_id = order_id
        self.instrument = instrument
        self.side = side
        self.price = price
        self.quantity = quantity
        self.status = status

