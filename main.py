#Program sederhana Rental Mobil Ainur Rafi

#  Data untuk rental mobil
mobil_list = [
    {"ID": 1, "Nama": "Toyota Avanza", "Status": "Tersedia"},
    {"ID": 2, "Nama": "Honda Jazz", "Status": "Disewa"},
    {"ID": 3, "Nama": "Suzuki Ertiga", "Status": "Tersedia"}
]

# Fungsi untuk menambah data mobil
def tambah_mobil():
    id_mobil = int(input("Masukkan ID mobil: "))
    nama_mobil = input("Masukkan nama mobil: ")
    status_mobil = input("Masukkan status mobil (Tersedia/Disewa): ")
    mobil_list.append({"ID": id_mobil, "Nama": nama_mobil, "Status": status_mobil})
    print("Mobil berhasil ditambahkan!")

# Fungsi untuk mencari data mobil
def cari_mobil():
    id_mobil = int(input("Masukkan ID mobil yang ingin dicari: "))
    for mobil in mobil_list:
        if mobil["ID"] == id_mobil:
            print(f'ID: {mobil["ID"]}, Nama: {mobil["Nama"]}, Status: {mobil["Status"]}')
            return
    print("Mobil tidak ditemukan.")

# Fungsi untuk merubah data mobil
def ubah_mobil():
    id_mobil = int(input("Masukkan ID mobil yang ingin diubah: "))
    for mobil in mobil_list:
        if mobil["ID"] == id_mobil:
            nama_mobil = input(f'Masukkan nama baru untuk mobil (nama lama: {mobil["Nama"]}): ')
            status_mobil = input(f'Masukkan status baru untuk mobil (status lama: {mobil["Status"]}): ')
            mobil["Nama"] = nama_mobil
            mobil["Status"] = status_mobil
            print("Data mobil berhasil diubah!")
            return
    print("Mobil tidak ditemukan.")

# Fungsi untuk menampilkan data mobil
def tampilkan_mobil():
    if not mobil_list:
        print("Tidak ada data mobil.")
    else:
        for mobil in mobil_list:
            print(f'ID: {mobil["ID"]}, Nama: {mobil["Nama"]}, Status: {mobil["Status"]}')

# Fungsi untuk menghapus data mobil
def hapus_mobil():
    id_mobil = int(input("Masukkan ID mobil yang ingin dihapus: "))
    for mobil in mobil_list:
        if mobil["ID"] == id_mobil:
            mobil_list.remove(mobil)
            print("Mobil berhasil dihapus!")
            return
    print("Mobil tidak ditemukan.")

# Pengulangan untuk menampilkan menu dan mengarahkan ke fungsi yang sesuai
print("Program sederhana Rental Mobil Ainur Rafi")
while True:
    print("\nMenu Utama:")
    print("1. Tambah data mobil baru")
    print("2. Mencari data mobil")
    print("3. Merubah data mobil")
    print("4. Menampilkan data semua data mobil")
    print("5. Menghapus data mobiil")
    print("6. Keluar")
        
    pilihan = input("Masukkan pilihan Anda: ")
        
    if pilihan == '1':
        tambah_mobil()
    elif pilihan == '2':
        cari_mobil()
    elif pilihan == '3':
        ubah_mobil()
    elif pilihan == '4':
        tampilkan_mobil()
    elif pilihan == '5':
        hapus_mobil()
    elif pilihan == '6':
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

