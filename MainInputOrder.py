from Order import Order
from OrderProcessor import OrderProcessor

# Buat processor
processor = OrderProcessor()

# Tentukan berapa order yang mau diinput
jumlah = int(input("Masukkan jumlah order: "))

for i in range(jumlah):
    print(f"\nInput Order ke-{i+1}")
    
    order_id = input("Masukkan Order ID: ")
    customer_name = input("Masukkan Nama Customer: ")
    order_date = input("Masukkan Tanggal (YYYY-MM-DD): ")
    total_amount = float(input("Masukkan Total Amount: "))

    # Buat object Order dari input
    order = Order(order_id, customer_name, order_date, total_amount)
    
    # Tambahkan ke processor
    processor.add_order(order)

# Tampilkan semua order
print("\n___| LIST ORDER |___")
processor.display_orders()

# Hitung total
print("\nTotal Revenue:", processor.calculate_total_revenue())
print("Total Tax (10%):", processor.calculate_total_tax(0.1))