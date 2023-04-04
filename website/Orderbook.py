import datetime


class Orderbook:
    def __init__(self):
        self.orders = {'buy': [], 'sell': []}

    def new_order(self, order):
        side = order[side]
        self.orders[side].append(order)


    def cancel_order(self, order_id):
        for side in ['buy', 'sell']:
            for order in self.orders[side]:
                if order.id == order_id:
                    self.orders[side].remove(order)
                    

    
    def get_order_status(self, order_id):
        for order in self.orders:
            if order.id == order_id:
                return order.status


class Order:
    # Status refers to partially filled or fully filled
    def __init__(self, order_id, instrument, side, price, quantity, status):
        self.order_id = order_id
        self.instrument = instrument
        self.side = side
        self.price = price
        self.quantity = quantity
        self.status = status
