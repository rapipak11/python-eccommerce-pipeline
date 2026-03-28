# Task 2 (Membuat class OrderProcessor)
# membuat class OrderProcessor
class OrderProcessor:
    # untuk tempat penyimpanan task 1
    def __init__(self):
        self.orders = []

    # untuk mendambahkan pesanan
    def add_order(self, order):
        self.orders.append(order)

    # untuk menampilkan pesanan
    def display_orders(self):
        for order in self.orders:
            order.display_order()

    # untuk menghitung total pesanan
    def calculate_total_revenue(self):
        total = 0
        for order in self.orders:
            total += order.total_amount
        return total

    # untuk menghitung pajak pesanan 10%
    def calculate_total_tax(self, tax_rate):
        total_tax = 0
        for order in self.orders:
            total_tax += order.calculate_tax(tax_rate)
        return total_tax
