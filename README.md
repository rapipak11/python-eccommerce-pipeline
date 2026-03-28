# python-eccommerce-pipeline
git ini dibuat untuk tugas membuat aplikasi sederhana dengan python (DE batch 14 dibimbing)


1. Project ini merupakan simulasi sederhana pengelolaan pesanan menggunakan Python dengan konsep OOP.
2. konsep yang digunakan dengan encapsualtion (data yang digunakan dengan class Order OrderProcessor) menggunakan OOP

file yang dibuat 
1. Order.py (untuk pesanan baru)
   - class Order (tempat menempatkan fungsi)
   - fungsi inisiasi order (def __init__(self, order_id, customer_name, order_date, total_amount))
   - fungsi hitung pajak order(def calculate_tax(self, tax_rate))
   - fungi tampil order (def display_order(self))
  
2. OrderProcessor (untuk menyimpan pesanan yang telah dibuat <bisa lebih dari 1>)
   - class OrderProcessor (tempat menempatkan fungsi)
   - fungsi inisiasi penyimpanan dari class order (def __init__(self))
   - fungsi menambahkan order (def add_order(self, order))
   - fungsi menampilkan order dari class order (def display_order(self))
   - fungsi menghitung total pesanan (def calculate_total_revenue(self))
   - fungsi menghitung total pajak 10% (def calculate_total_tax(self, tax_rate))
  
3. MainOrder.py (menjalankan Program dari Order.py dan OrderProcessor)
4. MainInputOrder.py (sama seperti MainOrder.py, namun saya menambahkan inputan untuk order yang akan dibuat)

untuk pengerjaannya di MainOrder.py saya memasukan 2 data (order1 = ("ORD001", "Budi", "2026-03-28", 200000), order2 = ("ORD002", "Idub", "2026-03-29", 500000) dengan total harga 70.000 dan program berhasil menghitung pajak sebesar 10% sebesar 7.000 secara otomatis

untuk pengerhaan di MainInputOrder.py, saya tentukan terlebih dahulu jumlah data yang akan diinputkan, kemudian diinputkan di form yang akan diisi (    
    order_id = input("Masukkan Order ID: ")
    customer_name = input("Masukkan Nama Customer: ")
    order_date = input("Masukkan Tanggal (YYYY-MM-DD): ")
    total_amount = float(input("Masukkan Total Amount: ")) 
setelah itu akan muncul total dan pajak 10% secara otomatis.
