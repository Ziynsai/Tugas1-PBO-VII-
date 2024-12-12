import mysql.connector

# Koneksi ke database
conn = mysql.connector.connect(
    user="root",
    host="localhost",
    password="",
    database="penjualan"
)

cur = conn.cursor()

# Membuat tabel jika belum ada
cur.execute("""
    CREATE TABLE IF NOT EXISTS Pegawai (
        NIK CHAR(25) NOT NULL PRIMARY KEY,
        Nama_Pegawai VARCHAR(50),
        Alamat_Pegawai VARCHAR(100)
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS Produk (
        Kode_Produk CHAR(25) NOT NULL PRIMARY KEY,
        Nama_Produk VARCHAR(50),
        Jumlah_Produk INT,
        Harga_Produk INT
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS Transaksi (
        No_Transaksi CHAR(25) NOT NULL PRIMARY KEY,
        Detail_Transaksi VARCHAR(100),
        NIK CHAR(25) NOT NULL,
        Kode_Produk CHAR(25) NOT NULL,
        FOREIGN KEY (NIK) REFERENCES Pegawai(NIK),
        FOREIGN KEY (Kode_Produk) REFERENCES Produk(Kode_Produk)
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS Struk (
        No_Transaksi CHAR(25) NOT NULL PRIMARY KEY,
        Nama_Pegawai VARCHAR(50),
        Nama_Produk VARCHAR(50),
        Jumlah_Produk INT,
        Total_Harga INT,
        FOREIGN KEY (No_Transaksi) REFERENCES Transaksi(No_Transaksi)
    )
""")

print("Tabel berhasil dibuat.")

while True:
    print("\n===== Aplikasi Kasir =====")
    print("1. Manajemen Data")
    print("2. Melakukan Transaksi")
    print("3. Laporan")
    print("4. Struk")
    print("5. Keluar")

    menu = input("Masukkan pilihan : ")

    if menu == '1':
        while True:
            print("\n===== Manajemen Data =====")
            print("1. Pegawai")
            print("2. Produk")
            print("3. Kembali")

            sub_menu = input("Masukkan pilihan : ")

            if sub_menu == '1':
                while True:
                    print("\n===== Manajemen Pegawai =====")
                    print("1. Tambah Pegawai")
                    print("2. Hapus Pegawai")
                    print("3. Tampilkan Pegawai")
                    print("4. Kembali")

                    pegawai_menu = input("Masukkan pilihan : ")
                    if pegawai_menu == '1':
                        print("\n===== Tambah Pegawai =====")
                        NIK = input("Masukkan NIK : ")
                        Nama_Pegawai = input("Masukkan Nama Pegawai : ")
                        Alamat = input("Masukkan Alamat : ")
                        cur.execute("""
                            INSERT INTO Pegawai (NIK, Nama_Pegawai, Alamat_Pegawai) 
                            VALUES (%s, %s, %s)""", 
                        (NIK, Nama_Pegawai, Alamat))
                        conn.commit()
                        print("Pegawai berhasil ditambahkan.")

                    elif pegawai_menu == '2':
                        print("\n===== Hapus Pegawai =====")
                        NIK = input("Masukkan NIK : ")
                        cur.execute("DELETE FROM Pegawai WHERE NIK = %s", (NIK,))
                        conn.commit()
                        print("Pegawai berhasil dihapus.")
                    elif pegawai_menu == '3':
                        print("\n===== Tampilkan Pegawai =====")
                        cur.execute("SELECT * FROM Pegawai")
                        pegawai = cur.fetchall()
                        for data in pegawai:
                            print(data)

                    elif pegawai_menu == '4':
                        break  # Kembali ke Manajemen Data

            elif sub_menu == '2':
                while True:
                    print("\n===== Manajemen Produk =====")
                    print("1. Tambah Produk")
                    print("2. Hapus Produk")
                    print("3. Tampilkan Produk")
                    print("4. Kembali")

                    produk_menu = input("Masukkan pilihan : ")
                    if produk_menu == '1':
                        print("\n===== Tambah Produk =====")
                        Kode_Produk = input("Masukkan Kode Produk : ")
                        Nama_Produk = input("Masukkan Nama Produk : ")
                        Jumlah_Produk = int(input("Masukkan Jumlah Produk : "))
                        Harga_Produk = int(input("Masukkan Harga Produk : "))
                        cur.execute("""
                            INSERT INTO Produk (Kode_Produk, Nama_Produk, Jumlah_Produk, Harga_Produk) 
                            VALUES (%s, %s, %s, %s)""", 
                        (Kode_Produk, Nama_Produk, Jumlah_Produk, Harga_Produk))
                        conn.commit()
                        print("Produk berhasil ditambahkan.")

                    elif produk_menu == '2':
                        print("\n===== Hapus Produk =====")
                        Kode_Produk = input("Masukkan Kode Produk : ")
                        cur.execute("DELETE FROM Produk WHERE Kode_Produk = %s", (Kode_Produk,))
                        conn.commit()
                        print("Produk berhasil dihapus.")

                    elif produk_menu == '3':
                        print("\n===== Tampilkan Produk =====")
                        cur.execute("SELECT * FROM Produk")
                        produk = cur.fetchall()
                        for data in produk:
                            print(data)

                    elif produk_menu == '4':
                        break

            elif sub_menu == '3':
                break

    elif menu == '2':
        print("\n===== Melakukan Transaksi =====")

        print("\n ==== Tampilan Data Barang ==== ")
        cur.execute("SELECT Kode_Produk, Nama_Produk, Harga_Produk FROM Produk")
        barang = cur.fetchall()
        for data in barang:
            print(f"ID: {data[0]}, Nama: {data[1]}, Harga: {data[2]}")

        print("\n ==== Tampilkan Data Pegawai ====")
        cur.execute("SELECT NIK, Nama_Pegawai FROM Pegawai")
        pegawai = cur.fetchall()
        for data in pegawai:
            print(f"NIK: {data[0]}, Nama: {data[1]}")

        print("\n==== Buat Pembelian ====")
        No_Transaksi = input("Masukkan nomor transaksi : ")
        NIK = input("Masukkan NIK Pegawai : ")
        Kode_Produk = input("Masukkan Kode Produk : ")
        Jumlah_Produk = int(input("Masukkan Jumlah Produk : "))
        cur.execute("SELECT Harga_Produk, Jumlah_Produk FROM Produk WHERE Kode_Produk = %s", (Kode_Produk,))
        produk_info = cur.fetchone()
        if produk_info:
            harga_produk, jumlah_produk = produk_info
            if Jumlah_Produk <= jumlah_produk:
                Total_Harga = harga_produk * Jumlah_Produk

                cur.execute("""
                        INSERT INTO Transaksi (No_Transaksi, NIK, Kode_Produk) 
                        VALUES (%s, %s, %s)""", 
                    (No_Transaksi, NIK, Kode_Produk))
                cur.execute("""
                        INSERT INTO Struk (No_Transaksi, Nama_Pegawai, Nama_Produk, Jumlah_Produk, Total_Harga) 
                        VALUES (%s, (SELECT Nama_Pegawai FROM Pegawai WHERE NIK = %s), (SELECT Nama_Produk FROM Produk WHERE Kode_Produk = %s), %s, %s)""", 
                    (No_Transaksi, NIK, Kode_Produk, Jumlah_Produk, Total_Harga))
                
                # Update jumlah produk setelah transaksi
                new_jumlah_produk = jumlah_produk - Jumlah_Produk
                cur.execute("UPDATE Produk SET Jumlah_Produk = %s WHERE Kode_Produk = %s", (new_jumlah_produk, Kode_Produk))
                
                conn.commit()
                print("Pembelian berhasil dilakukan.")
            else:
                print("Jumlah produk tidak cukup.")
        else:
            print("Kode Produk tidak ditemukan.")

    elif menu == '3':
        print("\n===== Laporan =====")
        print("1. Laporan Penjualan")
        print("2. Laporan Stok")
        print("3. Keluar ")

        laporan_menu = input("Masukkan pilihan : ")

        if laporan_menu == '1':
            print("\n==== Laporan Penjualan ====")
            cur.execute("SELECT No_Transaksi, NIK, Kode_Produk FROM Transaksi")
            penjualan = cur.fetchall()
            for data in penjualan:
                NIK = data[1]
                Kode_Produk = data[2]

                cur.execute("SELECT Nama_Pegawai FROM Pegawai WHERE NIK = %s", (NIK,))
                nama_pegawai = cur.fetchone()
                cur.execute("SELECT Nama_Produk FROM Produk WHERE Kode_Produk = %s", (Kode_Produk,))
                nama_produk = cur.fetchone()

                if nama_pegawai and nama_produk:
                    print(f"No_Transaksi: {data[0]}, Nama_Pegawai: {nama_pegawai[0]}, Nama_Produk: {nama_produk[0]}")

        elif laporan_menu == '2':
            print("\n==== Laporan Stok ====")
            cur.execute("SELECT Kode_Produk, Nama_Produk, Jumlah_Produk FROM Produk")
            stok = cur.fetchall()
            for data in stok:
                print(f"Kode_Produk: {data[0]}, Nama_Produk: {data[1]}, Jumlah_Produk: {data[2]}")

        elif laporan_menu == '3':
            print("\nTerima kasih telah menggunakan aplikasi penjualan dan pembelian produk!")
            break

    elif menu == '4':
        print("\n ==== Tampilan Transaksi ==== ")
        cur.execute("SELECT No_Transaksi FROM Transaksi")
        transaksi = cur.fetchall()
        for data in transaksi:
            print(f"No_Transaksi: {data[0]}")

        print("\n==== Pembuatan Struk ====")
        No_Transaksi = input("Masukkan No_Transaksi: ")

        # Ambil detail transaksi berdasarkan No_Transaksi
        cur.execute("SELECT Detail_Transaksi, NIK, Kode_Produk FROM Transaksi WHERE No_Transaksi = %s", (No_Transaksi,))
        transaksi = cur.fetchone()
        if transaksi:
            Detail_Transaksi, NIK, Kode_Produk = transaksi

            # Ambil jumlah produk dari transaksi
            cur.execute("SELECT Jumlah_Produk FROM Struk WHERE No_Transaksi = %s", (No_Transaksi,))
            Jumlah_Produk = cur.fetchone()
            Jumlah_Produk = Jumlah_Produk[0] if Jumlah_Produk else 0  # Ambil nilai dari tuple

            # Ambil harga produk
            cur.execute("SELECT Harga_Produk FROM Produk WHERE Kode_Produk = %s", (Kode_Produk,))
            harga_produk = cur.fetchone()
            harga_produk = harga_produk[0] if harga_produk else 0  # Ambil nilai dari tuple

            if harga_produk:
                Total_Harga = Jumlah_Produk * harga_produk

                # Ambil nama pegawai
                cur.execute("SELECT Nama_Pegawai FROM Pegawai WHERE NIK = %s", (NIK,))
                nama_pegawai = cur.fetchone()

                # Ambil nama produk
                cur.execute("SELECT Nama_Produk FROM Produk WHERE Kode_Produk = %s", (Kode_Produk,))
                nama_produk = cur.fetchone()

                # Tampilkan struk dengan format yang lebih menarik
                print("\n==== STRUK PEMBELIAN ====")
                print("=" * 30)
                print(f"No Transaksi     : {No_Transaksi}")
                print(f"Nama Pegawai     : {nama_pegawai[0] if nama_pegawai else 'Data tidak ditemukan'}")
                print(f"Nama Produk      : {nama_produk[0] if nama_produk else 'Data tidak ditemukan'}")
                print(f"Jumlah Produk    : {Jumlah_Produk}")
                print(f"Total Harga      : Rp {Total_Harga:,}")
                print("=" * 30)

                # Simpan struk ke dalam tabel Struk hanya jika belum ada
                cur.execute("SELECT * FROM Struk WHERE No_Transaksi = %s", (No_Transaksi,))
                if cur.fetchone() is None:  # Cek apakah struk sudah ada
                    try:
                        cur.execute("""
                            INSERT INTO Struk (No_Transaksi, Nama_Pegawai, Nama_Produk, Jumlah_Produk, Total_Harga) 
                            VALUES (%s, %s, %s, %s, %s)
                        """, (No_Transaksi, nama_pegawai[0] if nama_pegawai else None, 
                            nama_produk[0] if nama_produk else None, Jumlah_Produk, Total_Harga))
                        conn.commit()
                        print("Struk berhasil disimpan.")
                    except mysql.connector.IntegrityError as e:
                        print(f"Error: {e}. No Transaksi sudah ada.")
                else:
                    print("Struk sudah ada, tidak perlu disimpan lagi.")
            else:
                print("Harga produk tidak ditemukan.")
        else:
            print("Transaksi tidak ditemukan.")
    elif menu == '5':
        print("Keluar dari aplikasi.")
        break

cur.close()
conn.close()