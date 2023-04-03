from Orderbook import Order

class TradingPlatform:
    def __init__(self, exchanges, order_books):
        self.exchanges = exchanges
        self.order_books = order_books
        self.orders = {}

    #method to view orders from the order book
    def view_orders(self, username):
        # Get all orders for the user with the given username
        if not self.authentication(username):
            return "Authentication Failed"
        if username not in self.orders:
            return "No orders found for the user"
        orders = self.orders[username]
        return orders
    '''
    def view_orders(self, username):
        # Get all orders for the user with the given username
        pass
    '''
    '''
    #method to add order to the order book
    def add_order(self, username, order_id, instrument, order_type, quantity, price):
        # Add a new order for the user with the given username
        pass
    '''
    def add_order(self, username, order_id, instrument, order_type, quantity, price):
        # Add a new order for the user with the given username
        if not self.authentication(username):
            return "Authentication Failed"
        if order_id in self.orders:
            return "Order ID already exists"
        if instrument not in self.order_books:
            return "Invalid instrument"
        if order_type not in ["BUY", "SELL"]:
            return "Invalid order type!"

        #Create a new order object
        order = Order(order_id, instrument, order_type,
                      quantity, price, "New")

        if username not in self.orders:
            self.orders[username] = []
        self.orders[username].append(order)

        #Add the order to the order book
        order_book = self.order_books[instrument]
        if order_type == "BUY":
            order_book.new_order(order_id, price, quantity, "BUY", username)
        else:
            order

    '''
    def cancel_order(self, username, order_id):
        # Cancel an existing order for the user with the given username and order id
        pass
    '''
#method to cancel order from the order book
    def cancel_order(self, username, order_id):
        # Cancel an existing order for the user with the given username and order id
        if not self.authentication(username):
            return "Authentication Failed"
        if order_id not in self.orders:
            return "Order ID does not exist"
        order = self.orders[order_id]
        if order.status != "New":
            return "Order is not in New state"
        order.status = "Cancelled"
        order_book = self.order_books[order.instrument]
        order_book.cancel_order(order_id)
        return "Order cancelled successfully"
    
    #method to replace order from the order book
    def replace_order(self, username, order_id, new_order_type, new_quantity, new_price):
        # Replace an existing order for the user with the given username and order id
        if not self.authentication(username):
            return "Authentication Failed"
        if order_id not in self.orders:
            return "Order ID does not exist"
        order = self.orders[order_id]
        if order.status != "New":
            return "Order is not in New state"
        order.status = "Replaced"
        order_book = self.order_books[order.instrument]
        order_book.replace_order(order_id, new_order_type, new_quantity, new_price)
        return "Order replaced successfully"
    '''
    def replace_order(self, username, order_id, new_order_type, new_quantity, new_price):
        # Replace an existing order for the user with the given username and order id
        pass
    '''
    '''
    def slice_order(self, username, order_id):
        # Slice an existing order for the user with the given username and order id
        # Send the sliced orders to the SORT algorithm for execution
        pass
    '''
    #method to slice order from the order book
    def slice_order(self, username, order_id):
        # Slice an existing order for the user with the given username and order id
        # Send the sliced orders to the SORT algorithm for execution
        if not self.authentication(username):
            return "Authentication Failed"
        if order_id not in self.orders:
            return "Order ID does not exist"
        order = self.orders[order_id]
        if order.status != "New":
            return "Order is not in New state"
        order.status = "Sliced"
        order_book = self.order_books[order.instrument]
        order_book.slice_order(order_id)
        return "Order sliced successfully"

    #method to view trade history from the order book
    def view_trade_history(self, username):
        # Get the trade history for all executed trades
        if not self.authentication(username):
            return "Authentication Failed"
        if username not in self.orders:
            return "No orders found for the user"
        orders = self.orders[username]
        trade_history = []
        for order in orders:
            if order.status == "Executed":
                trade_history.append(order)
        return trade_history
    '''
    def view_trade_history(self):
        # Get the trade history for all executed trades
        pass
    '''

platform = TradingPlatform()

platform.add_exchange("NSE", "National Stock Exchange")
platform.add_exchange("BSE", "Bombay Stock Exchange")
platform.add_exchange("MCX", "Multi Commodity Exchange")
platform.add_exchange("LSE", "London Stock Exchange")

platform.add_order_book("AAPL", )

