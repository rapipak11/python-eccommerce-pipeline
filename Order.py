# Task 1 (membuat class order)
# membuat class Order
class Order:
    # fungsi inisiasi untuk penerima tamu
    def __init__(self, order_id, customer_name, order_date, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_date = order_date
        self.total_amount = total_amount

    # fungsi perhitungan pajak dari pemesanan
    def calculate_tax(self, tax_rate):
        return self.total_amount * tax_rate

    # fungsi menampilkan order
    def display_order(self):
        print(
            f"ID: {self.order_id} | Nama: {self.customer_name} | Tanggal: {self.order_date} |Total: {self.total_amount}"
        )
