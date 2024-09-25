import math

# iNI RUMUS UNTUK LIMAS SEGITIGA
def volume_limas_segitiga(panjang_alas, lebar_alas, tinggi):
    return (1/3) * (panjang_alas * lebar_alas) * tinggi

# INI RUMUS UNTUK SILINDER
def volume_silinder(jari_jari, tinggi):
    return math.pi * (jari_jari ** 2) * tinggi

while True:
    print(" ///////////////////////////////////////////////// ")
    print(" ====    Perhitungan Matematika 3 Dimensi    ====  ")
    print(" ///////////////////////////////////////////////// ")
    print(" = 1. Limas Segitiga                             = ")
    print("---------------------------------------------------")
    print(" = 2. Silinder                                   = ")
    print(" ///////////////////////////////////////////////// ")

    pilihan = input("Masukkan pilihan 1/2: ")

    if pilihan == "1":
        print("[ Limas Segitiga ]")
        panjang_alas = float(input("Masukkan panjang alas limas segitiga: "))
        lebar_alas = float(input("Masukkan lebar alas limas segitiga: "))
        tinggi_limas = float(input("Masukkan tinggi limas segitiga: "))
        volume_limas = volume_limas_segitiga(panjang_alas, lebar_alas, tinggi_limas)
        print(f"Volume limas segitiga: {volume_limas:.2f} unit kubik")

    elif pilihan == "2":
        print("[ Silinder ]")
        jari_jari = float(input("Masukkan jari-jari silinder: "))
        tinggi_silinder = float(input("Masukkan tinggi silinder: "))
        volume_silinder_result = volume_silinder(jari_jari, tinggi_silinder)
        print(f"Volume silinder: {volume_silinder_result:.2f} unit kubik")

    else:
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
