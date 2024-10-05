class DaftarMenu:
    def __init__(self):
        self.menu_makanan = {
            "Nasi Goreng": 15000,
            "Sate Ayam": 20000,
            "Mie Goreng": 12000
        }
        self.menu_minuman = {
            "Es Teh": 5000,
            "Kopi": 10000,
            "Air Mineral": 3000
        }

    def tampilkan_menu_makanan(self):
        print("\n==== Daftar Menu Makanan ====")
        if not self.menu_makanan:
            print("Tidak ada makanan dalam menu")
        else:
            for makanan, harga in self.menu_makanan.items():
                print(f"{makanan}: Rp{harga}")

    def tampilkan_menu_minuman(self):
        print("\nDaftar Menu Minuman:")
        if not self.menu_minuman:
            print("Tidak ada menu minuman.")
        else:
            for minuman, harga in self.menu_minuman.items():
                print(f"{minuman}: Rp{harga}")

    def tambah_menu_makanan(self, makanan, harga):
        self.menu_makanan[makanan] = harga
        print(f"{makanan} telah ditambahkan ke menu makanan dengan harga Rp{harga}.")

    def tambah_menu_minuman(self, minuman, harga):
        self.menu_minuman[minuman] = harga
        print(f"{minuman} telah ditambahkan ke menu minuman dengan harga Rp{harga}.")

def main():
    daftar_menu = DaftarMenu()

    while True:
        print("====    Daftar Menu Resto Rimuru sama   ====")
        print("==== 1. Tampilkan Menu Makanan          ====")
        print("==== 2. Tampilkan Menu Minuman          ====")
        print("==== 3. Tambah Menu Makanan dan Minuman ====")
        print("==== 4. Keluar                          ====")
        
        pilihan = input("Pilih opsi (1-4): ")

        if pilihan == '1':
            daftar_menu.tampilkan_menu_makanan()

        elif pilihan == '2':
            daftar_menu.tampilkan_menu_minuman()

        elif pilihan == '3':
            print ("==== DAFTAR TAMBAH MAKANAN DAN MINUMAN ====")
            print ("==== 1. Menambahkan Makanan            ====")
            print ("==== 2. Menambahkan Minuman            ====")

            tambah = input("Pilih opsi (1-2): ")

            if tambah == '1':
                makanan = input("Masukkan nama makanan: ")
                harga = int(input("Masukkan harga makanan: "))
                daftar_menu.tambah_menu_makanan(makanan, harga)

            elif tambah =='2':
                minuman = input("Masukkan nama minuman: ")
                harga = int(input("Masukkan harga minuman: "))
                daftar_menu.tambah_menu_minuman(minuman, harga)
            else:
                print("Input tidak valid")

        elif pilihan == '4':
            print("ADIOS, OMAE WA MO SHINDEIRU")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
