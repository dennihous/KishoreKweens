from Orderbook import Orderbook

class Exchange:
    def __init__(self, name, fee_ladder):
        self.name = name
        self.fee_ladder = fee_ladder
        self.order_books = {}

    def add_order_book(self, instrument):
        self.order_books[instrument] = OrderBook(instrument)

    def get_order_book(self, instrument):
        return self.order_books.get(instrument)

   
   #method to calculate fee
    def calculate_fee(self, order):
        # Calculate fee based on the exchange's fee ladder and order details
        # Return the fee amount
        pass
    '''
    def calculate_fee(self, order):
        # Calculate fee based on the exchange's fee ladder and order details
        # Return the fee amount
        pass
    '''