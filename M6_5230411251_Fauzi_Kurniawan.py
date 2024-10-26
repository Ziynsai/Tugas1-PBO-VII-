class Order:
    def __init__(self, ID, name, details):
        self._ID = ID
        self.name = name
        self.details = details

    def setOrder(self, name, details):
        self.name = name
        self.details = details

    def tampilkan_Order(self):
        return f"ID: {self._ID}, Nama Order: {self.name}, Details: {self.details}"
    
    def hapus_Order(self):
        return f"Order {self.name} (ID: {self._ID}) telah dihapus."


class Delivery:
    def __init__(self, id, name):
        self._id = id
        self.name = name

    def processDelivery(self, information, date, address):
        self.information = information
        self.date = date
        self.address = address

    def tampilkan_Delivery(self):
        return f"ID: {self._id}, Nama: {self.name}, Informasi: {self.information}, Tanggal: {self.date}, Alamat: {self.address}"
    
    def hapus_Delivery(self):
        return f"Delivery {self.name} (ID: {self._id}) telah dihapus."


order_list = []
address_list = []

while True:
    print("\n1. Order")
    print("2. Delivery")
    print("3. Exit")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("\n======= Order =======")
        print("1. Add Order")
        print("2. View Order")
        print("3. Delete Order")
        print("4. Back")
        pilihan_order = input("Pilih menu: ")

        if pilihan_order == "1":
            nama = str(input("Masukkan nama order: "))
            details = str(input("Masukkan details order: "))
            order = Order(len(order_list) + 1, nama, details)
            order_list.append(order)
            print(f"Order {nama} berhasil ditambahkan")

        elif pilihan_order == "2":
            for order in order_list:
                print(order.tampilkan_Order())

        elif pilihan_order == "3":
            id_to_delete = int(input("Masukkan ID order yang ingin dihapus: "))
            order_to_delete = next((o for o in order_list if o._ID == id_to_delete), None)
            if order_to_delete:
                order_list.remove(order_to_delete)
                print(order_to_delete.hapus_Order())
            else:
                print("Order tidak ditemukan.")

    elif pilihan == "2":
        print("\n======= Delivery =======")
        print("1. Add Delivery")
        print("2. View Delivery")
        print("3. Delete Delivery")
        print("4. Back")
        pilihan_delivery = input("Pilih menu: ")

        if pilihan_delivery == "1":
            nama = str(input("Masukkan nama delivery: "))
            informasi = str(input("Masukkan informasi delivery: "))
            tanggal = str(input("Masukkan tanggal delivery: "))
            alamat = str(input("Masukkan alamat delivery: "))
            delivery = Delivery(len(address_list) + 1, nama)
            delivery.processDelivery(informasi, tanggal, alamat)
            address_list.append(delivery)
            print(f"Delivery {nama} berhasil ditambahkan")

        elif pilihan_delivery == "2":
            for delivery in address_list:
                print(delivery.tampilkan_Delivery())

        elif pilihan_delivery == "3":
            id_to_delete = int(input("Masukkan ID delivery yang ingin dihapus: "))
            delivery_to_delete = next((d for d in address_list if d._id == id_to_delete), None)
            if delivery_to_delete:
                address_list.remove(delivery_to_delete)
                print(delivery_to_delete.hapus_Delivery())
            else:
                print("Delivery dengan ID tidak ditemukan.")

    elif pilihan == "3":
        print("Udah duluan ya bre, Admin mau nonton anime")
        break
