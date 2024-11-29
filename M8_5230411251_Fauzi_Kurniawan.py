import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os


class AppOrder:
    def __init__(self, root):
        self.root = root
        self.root.title("Tools PADKA 1.0")
        self.root.geometry("1000x800")
        self.root.configure(bg="#87CEEB")  # Warna biru langit
        self.widget_create()

    def widget_create(self):
        # Header
        title_frame = tk.Frame(self.root, bg="#4682B4")  # Warna biru baja
        title_frame.pack(pady=10, fill="x")

        Judul_Tema = tk.Label(
            title_frame,
            text="Tools Perhitungan Air Desa dan Keluhan Air",
            font=("Hanken Grotesk", 24, 'bold'),
            bg="#4682B4",
            fg="white"
        )
        Judul_Tema.pack(pady=10)

        # Input Frame
        input_frame = tk.Frame(self.root, bg="#87CEEB")
        input_frame.pack(pady=20)

        # Nama Pemilik Rumah
        name_label = tk.Label(
            input_frame,
            text="Nama Pemilik Rumah: ",
            bg="#87CEEB",
            fg="black",
            font=("Arial", 12)
        )
        name_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.name_entry = tk.Entry(input_frame, width=30, font=("Arial", 12))
        self.name_entry.grid(row=0, column=1, pady=5)

        # Debit Air
        debit_label = tk.Label(
            input_frame,
            text="Debit Air dalam 1 Bulan (m³): ",
            bg="#87CEEB",
            fg="black",
            font=("Arial", 12)
        )
        debit_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.debit_entry = tk.Entry(input_frame, width=30, font=("Arial", 12))
        self.debit_entry.grid(row=1, column=1, pady=5)

        # Keluhan
        keluhan_label = tk.Label(
            input_frame,
            text="Pilih Keluhan: ",
            bg="#87CEEB",
            fg="black",
            font=("Arial", 12)
        )
        keluhan_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.Opsi_Keluhan = ["Kualitas Air", "Masalah Tagihan"]
        self.Keluhan_Menu = ttk.Combobox(
            input_frame,
            values=self.Opsi_Keluhan,
            width=28,
            state="readonly",
            font=("Arial", 12)
        )
        self.Keluhan_Menu.grid(row=2, column=1, pady=5)
        self.Keluhan_Menu.set("Pilih Keluhan")

        # Tombol Tambah Data
        self.pesan_button = tk.Button(
            input_frame,
            text="Tambah Data",
            command=self.tambah_data,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12)
        )
        self.pesan_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Tabel Data
        order_data = tk.Label(
            self.root,
            text="Daftar Data",
            font=("Helvetica", 18, 'bold'),
            bg="#87CEEB",
            fg="black"
        )
        order_data.pack()

        # digunakan untuk columb di tampilan
        self.data_Tabel = ttk.Treeview(
            self.root,
            columns=("Nama Pemilik", "Debit Air (m³)", "Total Pembayaran", "Keluhan"),
            show="headings"
        )
        self.data_Tabel.heading("Nama Pemilik", text="Nama Pemilik")
        self.data_Tabel.heading("Debit Air (m³)", text="Debit Air (m³)")
        self.data_Tabel.heading("Total Pembayaran", text="Total Pembayaran")
        self.data_Tabel.heading("Keluhan", text="Keluhan")

        self.data_Tabel.column("Nama Pemilik", width=200, anchor="center")
        self.data_Tabel.column("Debit Air (m³)", width=200, anchor="center")
        self.data_Tabel.column("Total Pembayaran", width=200, anchor="center")
        self.data_Tabel.column("Keluhan", width=200, anchor="center")
        self.data_Tabel.pack(pady=10)

        # Tombol simpan
        button_frame = tk.Frame(self.root, bg="#87CEEB")
        button_frame.pack(pady=10)

        # intinya ini bagian kayak css
        self.save_button = tk.Button(
            button_frame,
            text="Simpan ke Excel",
            command=self.save_to_excel,
            bg="#2196F3",
            fg="white",
            font=("Arial", 12)
        )
        self.save_button.grid(row=0, column=0, padx=10)

        # ini untuk tombol hapus data
        self.delete_button = tk.Button(
            button_frame,
            text="Hapus Data",
            command=self.hapus_data,
            bg="#FF4500",
            fg="white",
            font=("Arial", 12)
        )
        self.delete_button.grid(row=0, column=1, padx=10)

        self.search_button = tk.Button(
            button_frame,
            text="Cari Data",
            command=self.cari_data,
            bg="#FFC107",
            fg="black",
            font=("Arial", 12)
        )
        self.search_button.grid(row=0, column=2, padx=10)

    def tambah_data(self):
        name = self.name_entry.get()
        debit = self.debit_entry.get()
        keluhan = self.Keluhan_Menu.get()

        try:
            debit = float(debit)
            if debit <= 0:
                raise ValueError("Debit harus lebih dari 0.")
            if name and keluhan != "Pilih Keluhan":
                total_pembayaran = f"Rp {debit * 500:,.0f}".replace(',', '.')
                self.data_Tabel.insert("", "end", values=(name, debit, total_pembayaran, keluhan))
                self.name_entry.delete(0, tk.END)
                self.debit_entry.delete(0, tk.END)
                self.Keluhan_Menu.set("Pilih Keluhan")
            else:
                messagebox.showerror("Error", "Semua kolom harus diisi dengan benar.")
        except ValueError as e:
            messagebox.showerror("Error", f"Kesalahan input: {e}")

    def hapus_data(self):
        # Hapus item dengan menekan bagian mana yang ingin dihapus
        selected_item = self.data_Tabel.selection()
        if selected_item:
            for item in selected_item:
                self.data_Tabel.delete(item)
        else:
            messagebox.showerror("Error", "Pilih data yang ingin dihapus.")

    def save_to_excel(self):
        # Digunakkan untuk mendapatkan item dari data_tabel
        data = []
        for item in self.data_Tabel.get_children():
            data.append(self.data_Tabel.item(item)['values'])

        if not data:
            messagebox.showerror("Error", "Tidak ada data untuk disimpan.")
            return
        
        # Intinya ini membuat kolom di exel
        df = pd.DataFrame(data, columns=["Nama Pemilik Rumah", "Debit Air (m³)", "Total Pembayaran", "Keluhan"])

        documents_path = os.path.expanduser("C:\coba") # lOKASI PENYIMPANAN 
        data_folder = os.path.join(documents_path, "Data")
        os.makedirs(data_folder, exist_ok=True)
        file_path = os.path.join(data_folder, "Data Air Desa 2024.xlsx")

        #Pemberitahuan jika metode simpan berhasil atau tidak
        try:
            df.to_excel(file_path, index=False, engine='openpyxl')
            messagebox.showinfo("Sukses", f"Data berhasil disimpan ke {file_path}!")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

    def cari_data(self):
        # Membuka jendela input untuk meminta nama pemilik rumah
        cari_window = tk.Toplevel(self.root)
        cari_window.title("Cari Data")
        cari_window.geometry("400x150")
        cari_window.configure(bg="#87CEEB")

        # Label dan entry digunakkan untuk mencari pemilik rumah
        label = tk.Label(cari_window, text="Masukkan Nama Pemilik Rumah:", bg="#87CEEB", font=("Arial", 12))
        label.pack(pady=10)

        nama_input = tk.Entry(cari_window, width=30, font=("Arial", 12))
        nama_input.pack(pady=5)

        # code ini digunakkan untuk mencari 
        def search():
            nama_cari = nama_input.get().strip()
            for item in self.data_Tabel.get_children():
                values = self.data_Tabel.item(item)['values']
                if nama_cari.lower() in str(values[0]).lower():
                    self.data_Tabel.selection_set(item) # Digunakkan untuk menyoroti 
                    self.data_Tabel.see(item)  # cuma untuk memastikan tampilannya ada
                    messagebox.showinfo("Hasil Pencarian", f"Data ditemukan: {values}")
                    cari_window.destroy()
                    return
            messagebox.showerror("Tidak Ditemukan", f"Tidak ada data dengan nama: {nama_cari}")
            cari_window.destroy()

        # Tombol untuk cari
        search_button = tk.Button(cari_window, text="Cari", command=search, bg="#4CAF50", fg="white", font=("Arial", 12))
        search_button.pack(pady=10)

        # Tombol untuk cencel
        cancel_button = tk.Button(cari_window, text="Batal", command=cari_window.destroy, bg="#FF4500", fg="white", font=("Arial", 12))
        cancel_button.pack(pady=5)

root = tk.Tk()
app = AppOrder(root)
root.mainloop()
