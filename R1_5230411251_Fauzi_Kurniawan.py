class Pegawai:
    def __init__(self, nik, nama, alamat):
        self.__nik = nik  
        self.nama = nama
        self.alamat = alamat

    def get_nik(self):
        return self.__nik

class Transaksi:
    def __init__(self, no_transaksi, pegawai):
        self.no_transaksi = no_transaksi
        self.pegawai = pegawai
        self.detail_transaksi = []
    
    def tambah_detail(self, produk, jumlah):
        self.detail_transaksi.append((produk, jumlah))
    
    def total_harga(self):
        return sum(produk.harga * jumlah for produk, jumlah in self.detail_transaksi)

class Struk:
    def __init__(self, transaksi):
        self.no_transaksi = transaksi.no_transaksi
        self.nama_pegawai = transaksi.pegawai.nama
        self.detail_struk = transaksi.detail_transaksi
        self.total_harga = transaksi.total_harga()

    def cetak_struk(self):
        print(f"\nNo. Transaksi: {self.no_transaksi}")
        print(f"Nama Pegawai: {self.nama_pegawai}")
        print("Detail Produk:")
        for produk, jumlah in self.detail_struk:
            print(f"- {produk.nama_produk} x {jumlah} @ {produk.harga} = {produk.harga * jumlah}")
        print(f"Total Harga: {self.total_harga}")

class Produk:
    def __init__(self, kode_produk, nama_produk, jenis_produk, harga):
        self.__kode_produk = kode_produk  
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk
        self.harga = harga

    def get_kode_produk(self):
        return self.__kode_produk

    def __str__(self):
        return f"{self.nama_produk} ({self.jenis_produk}) - Rp {self.harga}"

class Snack(Produk):
    def __init__(self, nama_produk, harga):
        super().__init__(kode_produk="SNK", nama_produk=nama_produk, jenis_produk="Snack", harga=harga)

class Makanan(Produk):
    def __init__(self, nama_produk, harga):
        super().__init__(kode_produk="MKN", nama_produk=nama_produk, jenis_produk="Makanan", harga=harga)

class Minuman(Produk):
    def __init__(self, nama_produk, harga):
        super().__init__(kode_produk="MNM", nama_produk=nama_produk, jenis_produk="Minuman", harga=harga)

produk_snack = []
produk_makanan = []
produk_minuman = []
transaksi = []

while True:
    print("\n////// Menu Kelola //////")
    print("1. Tambah Produk")
    print("2. Tambah Transaksi")
    print("3. Cetak Struk")
    print("4. Keluar")
    pilihan = input("Pilih menu: ")
    
    if pilihan == '1':
        print("\n////// Menu Tambah Produk //////")
        print("1. Tambah Snack")
        print("2. Tambah Makanan")
        print("3. Tambah Minuman")
        print("0. Kembali Menu Kelola")
        pilihan_produk = input("Pilih produk: ")
        
        if pilihan_produk == "1":
            nama_produk = input("Masukkan nama produk: ")
            harga = int(input("Masukkan harga: "))
            snack = Snack(nama_produk, harga)
            produk_snack.append(snack)
            print(f"Snack {nama_produk} berhasil ditambahkan")

        elif pilihan_produk == "2":
            nama_produk = input("Masukkan nama produk: ")
            harga = int(input("Masukkan harga: "))
            makanan = Makanan(nama_produk, harga)
            produk_makanan.append(makanan)
            print(f"Makanan {nama_produk} berhasil ditambahkan")

        elif pilihan_produk == "3":
            nama_produk = input("Masukkan nama produk: ")
            harga = int(input("Masukkan harga: "))
            minuman = Minuman(nama_produk, harga)
            produk_minuman.append(minuman)
            print(f"Minuman {nama_produk} berhasil ditambahkan")

        elif pilihan_produk == "0":
            continue

        print("\nDaftar Snack:")
        for i, prod in enumerate(produk_snack):
            print(f"{i + 1}. {prod}")
        print("\nDaftar Makanan:")
        for i, prod in enumerate(produk_makanan):
            print(f"{i + 1}. {prod}")
        print("\nDaftar Minuman:")
        for i, prod in enumerate(produk_minuman):
            print(f"{i + 1}. {prod}")

    elif pilihan == '2':
        print("\n////// Menu Tambah Transaksi //////")
        print("1. Tambah Transaksi Baru")
        print("0. Kembali ke Menu Kelola")
        pilihan_transaksi = input("Pilih transaksi: ")
        
        if pilihan_transaksi == "1":
            no_transaksi = input("Masukkan no transaksi: ")
            nama_pegawai = input("Masukkan nama pegawai: ")
            alamat_pegawai = input("Masukkan alamat pegawai: ") 
            nik_pegawai = input("Masukkan NIK pegawai: ")  
            pegawai = Pegawai(nik=nik_pegawai, nama=nama_pegawai, alamat=alamat_pegawai)
            transaksi_baru = Transaksi(no_transaksi, pegawai)
            transaksi.append(transaksi_baru)

            while True:
                print("\nPilih produk untuk ditransaksikan:")
                print("1. Snack")
                print("2. Makanan")
                print("3. Minuman")
                print("0. Selesai")
                pilihan_produk = input("Pilih kategori produk: ")
                
                if pilihan_produk == '0':
                    break
                
                if pilihan_produk == '1':
                    for idx, prod in enumerate(produk_snack):
                        print(f"{idx + 1}. {prod}")
                    pilihan_item = int(input("Pilih snack: ")) - 1
                    jumlah = int(input("Masukkan jumlah: "))
                    if 0 <= pilihan_item < len(produk_snack):
                        transaksi_baru.tambah_detail(produk_snack[pilihan_item], jumlah)
                    else:
                        print("Snack tidak ditemukan.")

                elif pilihan_produk == '2':
                    for idx, prod in enumerate(produk_makanan):
                        print(f"{idx + 1}. {prod}")
                    pilihan_item = int(input("Pilih makanan: ")) - 1
                    jumlah = int(input("Masukkan jumlah: "))
                    if 0 <= pilihan_item < len(produk_makanan):
                        transaksi_baru.tambah_detail(produk_makanan[pilihan_item], jumlah)
                    else:
                        print("Makanan tidak ditemukan.")

                elif pilihan_produk == '3':
                    for idx, prod in enumerate(produk_minuman):
                        print(f"{idx + 1}. {prod}")
                    pilihan_item = int(input("Pilih minuman: ")) - 1
                    jumlah = int(input("Masukkan jumlah: "))
                    if 0 <= pilihan_item < len(produk_minuman):
                        transaksi_baru.tambah_detail(produk_minuman[pilihan_item], jumlah)
                    else:
                        print("Minuman tidak ditemukan.")
                    
                else:
                    print("Pilihan tidak valid. Silakan pilih lagi.")

        elif pilihan_transaksi == '0':
            continue 

    elif pilihan == '3':
        print("\n1. Cetak Daftar Transaksi")
        print("2. Cetak Struk Transaksi")
        print("0. Kembali ke Menu Kelola")
        pilihan_cetak = input("Pilih cetak: ")
        
        if pilihan_cetak == "1":
            for i, trx in enumerate(transaksi):
                print(f"No. {i + 1}. Transaksi {trx.no_transaksi} oleh {trx.pegawai.nama}")
        
        elif pilihan_cetak == "2":
            no_transaksi = input("Masukkan no transaksi untuk cetak struk: ")
            transaksi_terpilih = next((t for t in transaksi if t.no_transaksi == no_transaksi), None)
            
            if transaksi_terpilih:
                struk = Struk(transaksi_terpilih)
                struk.cetak_struk()
            else:
                print("Transaksi tidak ditemukan.")

        elif pilihan_cetak == '0':
            continue 

    elif pilihan == '4':
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
