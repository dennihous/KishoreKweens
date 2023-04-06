from trading_platform import TradingPlatform
from Orderbook import OrderBook

class TradingHistory:
    def view_trade_history(self, user_id):
        user_orders = self.users[user_id]['orders']
        trade_history = []
        for order in user_orders:
            if order['status'] == 'Executed':
                trade_history.append(order)
        return trade_history
