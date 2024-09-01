class StockTransaction:
    def __init__(self, stock_symbol, quantity, price):
        self.stock_symbol = stock_symbol
        self.quantity = quantity
        self.price = price

class TransactionValidator:
    def validate(self, transaction):
        # Misalnya validasi apakah jumlah saham cukup
        print(f"Validating transaction for {transaction.quantity} shares of {transaction.stock_symbol}.")
        return True

class TransactionExecutor:
    def execute(self, transaction):
        # Misalnya eksekusi transaksi
        print(f"Executing transaction for {transaction.quantity} shares of {transaction.stock_symbol} at ${transaction.price} each.")

class TransactionReportGenerator:
    def generate_report(self, transaction):
        # Misalnya pembuatan laporan
        print(f"Transaction report: {transaction.quantity} shares of {transaction.stock_symbol} bought at ${transaction.price} each.")

# Contoh penggunaan yang benar
transaction = StockTransaction("AAPL", 10, 150)

validator = TransactionValidator()
executor = TransactionExecutor()
report_generator = TransactionReportGenerator()

if validator.validate(transaction):
    executor.execute(transaction)
    report_generator.generate_report(transaction)
