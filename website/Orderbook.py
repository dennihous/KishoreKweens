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
                    

    def execute_trade(self):
        if not self.order['buy', 'sell']:
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
