class Debitur:
    def __init__(self, ktp, nama, limit_pinjaman):
        self.nama = nama
        self.__ktp = ktp
        self._limit_pinjaman = limit_pinjaman

    def tampilkan_debitur(self):
        return f"Nama Debitur: {self.nama}, No. KTP: {self.__ktp}, Limit Pinjaman: {self._limit_pinjaman}"

    def get_ktp(self):
        return self.__ktp

    def cari_debitur(debitur_list, nama):
        for debitur in debitur_list:
            if debitur.nama == nama:
                return f"Nama: {debitur.nama}, KTP: {debitur.get_ktp()}, Limit Pinjaman: {debitur._limit_pinjaman}"
        return "Debitur tidak ditemukan"

    def tambah_debitur(debitur_list, nama, ktp, limit_pinjaman):
        for debitur in debitur_list:
            if debitur.get_ktp() == ktp:
                return "Debitur sudah ada"
        new_debitur = Debitur(ktp, nama, limit_pinjaman)
        debitur_list.append(new_debitur)
        return f"Debitur {nama} sudah ditambahkan"


class KelolaPinjaman:
    def __init__(self, debitur, pokok, bunga, bulan):
        self.debitur = debitur
        self.pokok = pokok 
        self.bunga = bunga  
        self.bulan = bulan 
        self.total_angsuran, self.angsuran_bulanan = self.hitung_pinjaman()

    def hitung_pinjaman(self):
        bunga_total = self.pokok * (self.bunga / 100)
        total_angsuran = self.pokok + bunga_total
        angsuran_bulanan = total_angsuran / self.bulan
        return total_angsuran, angsuran_bulanan

    def tampilkan_pinjaman(self):
        return (f"Nama Debitur: {self.debitur.nama}, "
                f"Pokok: {self.pokok}, "
                f"Bunga: {self.bunga}%, "
                f"Total Angsuran: {self.total_angsuran:.2f}, "
                f"Angsuran Bulanan: {self.angsuran_bulanan:.2f}")


debitur_list = []
pinjam_list = []

# Sample data
debitur_list.append(Debitur("123", "Rimuru", 7000000))
debitur_list.append(Debitur("456", "Diablo", 4000000))
debitur_list.append(Debitur("789", "Ains", 8000000))
debitur_list.append(Debitur("335", "Tempest", 3000000))


while True:
    print("========== Aplikasi Admin Pinjol =========")
    print("1. Kelola Debitur")
    print("2. Pinjam")
    print("0. Keluar")

    pilihan = input("Pilih Menu: ")

    if pilihan == "1":
        print("\n========= Kelola Debitur =========")
        print("1. Tampilkan semua Debitur")
        print("2. Cari Debitur")
        print("3. Tambah Debitur")
        print("0. Kembali")
        pilihan2 = input("Pilih Menu: ")

        if pilihan2 == "1":
            print("\n========= Tampilkan semua Debitur =========")
            for debitur in debitur_list:
                print(debitur.tampilkan_debitur())
        
        elif pilihan2 == "2":
            print("\n========= Cari Debitur =========")
            nama = input("Masukkan Nama Debitur: ")
            hasil = Debitur.cari_debitur(debitur_list, nama)
            print(hasil)

        elif pilihan2 == "3":
            print("\n========= Tambah Debitur =========")
            nama = input("Masukkan Nama Debitur: ")
            ktp = input("Masukkan No.KTP Debitur: ")
            limit_pinjaman = input("Masukkan Limit Pinjaman: ")
            hasil = Debitur.tambah_debitur(debitur_list, nama, ktp, limit_pinjaman)
            print(hasil)

        elif pilihan2 == "0":
            print("Kembali ke menu utama")

    elif pilihan == "2":
        print("\n========= Menu Pinjam =========")
        print("1. Tambah Pinjaman")
        print("2. Tampilkan Pinjaman")
        print("0. Kembali")

        pilihan3 = input("Pilih Menu: ")

        if pilihan3 == "1":
            print("\n========= Tambah Pinjaman =========")
            nama = str(input("Masukkan Nama Debitur: "))
            ktp = int(input("Masukkan No.KTP Debitur: "))
            pokok = float(input("Masukkan Angka Pokok (Dalam Rupiah): "))
            bunga = float(input("Masukkan Bunga (Dalam Persen): "))
            bulan = int(input("Masukkan Lama Pinjaman (Dalam Bulan): "))
            
            debitur = next((d for d in debitur_list if d.get_ktp() == ktp), None)
            if debitur:
                new_pinjaman = KelolaPinjaman(debitur, pokok, bunga, bulan)
                pinjam_list.append(new_pinjaman)
                print("Pinjaman berhasil ditambahkan")
            else:
                print("Debitur tidak ditemukan.")

        elif pilihan3 == "2":
            print("\n========= Tampilkan Pinjaman =========")
            for pinjaman in pinjam_list:
                print(pinjaman.tampilkan_pinjaman())

        elif pilihan3 == "0":
            print("Kembali ke menu utama")

    elif pilihan == "0":
        print("Keluar dari aplikasi.")
        break
