class StockTransaction:
    def __init__(self, stock_symbol, quantity, price):
        self.stock_symbol = stock_symbol
        self.quantity = quantity
        self.price = price

    def validate_transaction(self):
        # Misalnya validasi apakah jumlah saham cukup
        print(f"Validating transaction for {self.quantity} shares of {self.stock_symbol}.")
        return True

    def execute_transaction(self):
        # Misalnya eksekusi transaksi
        print(f"Executing transaction for {self.quantity} shares of {self.stock_symbol} at ${self.price} each.")
    
    def generate_report(self):
        # Misalnya pembuatan laporan
        print(f"Transaction report: {self.quantity} shares of {self.stock_symbol} bought at ${self.price} each.")
    
# Contoh penggunaan yang salah
transaction = StockTransaction("AAPL", 10, 150)
if transaction.validate_transaction():
    transaction.execute_transaction()
    transaction.generate_report()