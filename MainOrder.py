#memanggil class Oder dan OrderProcessor
from Order import Order
from OrderProcessor import OrderProcessor

# Buat object order
order1 = Order("ORD001", "Budi", "2026-03-28", 200000)
order2 = Order("ORD002", "Idub", "2026-03-29", 500000)
# Buat processor
processor = OrderProcessor()

# Tambahkan order1 ke processor
processor.add_order(order1)
processor.add_order(order2)

# Tampilkan order1
print(" ___|LIST ORDER|___ ")
processor.display_orders()

# Hitung total revenue order1
print("\nTotal Revenue:", processor.calculate_total_revenue())
# Hitung total pajak 10%
print("Total Tax:", processor.calculate_total_tax(0.1))

