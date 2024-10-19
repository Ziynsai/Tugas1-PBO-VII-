class Music:
    def __init__(self, title, artist, genre):
        self.title = title
        self.artist = artist
        self.genre = genre

    def display(self):
        return f"{self.title} - {self.artist} - ({self.genre})"

class JapanaseAnime(Music):
    def __init__(self, title, artist):
        super().__init__(title, artist, "Anime")

class JapanaseRock(Music):
    def __init__(self, title, artist):
        super().__init__(title, artist, "Rock")

class HalalMusic(Music):
    def __init__(self, title, artist):
        super().__init__(title, artist, "Halal")

class KoleksiMusik:
    def __init__(self):
        self.collection = []

    def Menambahkan_music(self, music):
        self.collection.append(music)

    def delete_music(self, title):
        self.collection = [music for music in self.collection if music.title != title]

    def display_all(self, genre=None):
        if genre:
            filtered_collection = [music for music in self.collection if isinstance(music, genre)]
        else:
            filtered_collection = self.collection
        sorted_collection = sorted(filtered_collection, key=lambda x: x.title)
        for music in sorted_collection:
            print(music.display())

    def search_by_artist(self, artist):
        found_songs = [music for music in self.collection if music.artist.lower() == artist.lower()]
        for song in found_songs:
            print(song.display())

music_collection = KoleksiMusik()

# List anime song
music_collection.Menambahkan_music(JapanaseAnime("Unravel", "Toru Kitajima"))
music_collection.Menambahkan_music(JapanaseAnime("Inferno", "Green Apple"))
music_collection.Menambahkan_music(JapanaseAnime("Innocence", "Noisy Cell"))
music_collection.Menambahkan_music(JapanaseAnime("Can't You Say", "Roys"))
music_collection.Menambahkan_music(JapanaseAnime("Next to You", "Ken Arai"))

# List rock/metal song
music_collection.Menambahkan_music(JapanaseRock("Keep it Real", "One ok rock"))
music_collection.Menambahkan_music(JapanaseRock("Ambitions", "One ok rock"))
music_collection.Menambahkan_music(JapanaseRock("Da Da Dance", "Baby Metal"))
music_collection.Menambahkan_music(JapanaseRock("The One", "Baby Metal"))
music_collection.Menambahkan_music(JapanaseRock("Northern Hell Song", "Ryujin"))

# List halal song
music_collection.Menambahkan_music(HalalMusic("Halal Life", "Maher Zain"))
music_collection.Menambahkan_music(HalalMusic("Ya Nabi Salam Alayka", "Maher Zain"))
music_collection.Menambahkan_music(HalalMusic("Kun Anta", "Humood AlKhudher"))
music_collection.Menambahkan_music(HalalMusic("Assalamu Alayka", "Muhammad Tarek"))
music_collection.Menambahkan_music(HalalMusic("Where you are", "HalalBeats"))

while True:
    print("========== Playlist Music ==========")
    print("1. Japanese Anime song List ")
    print("2. Japanese Rock song List ")
    print("3. Halal song List ")
    print("4. Tambah Musik")
    print("5. Cari Musik berdasarkan Penyanyi")
    print("6. Hapus Musik")
    print("0. Keluar")
    print("====================================")

    pilihan = input("Masukkan pilihan anda: ")

    if pilihan == '1':
        print("\n==== Japanese Anime Song ====")
        music_collection.display_all(JapanaseAnime)

    elif pilihan == '2':
        print("\n==== Japanese Rock Song ====")
        music_collection.display_all(JapanaseRock)

    elif pilihan == '3':
        print("\n==== Halal Song ====")
        music_collection.display_all(HalalMusic)

    elif pilihan == '4':
        title = str(input("Masukkan judul lagu: "))
        artist = str(input("Masukkan penyanyi: "))
        genre = str(input("Masukkan genre (Anime/Rock/Halal): ").lower())

        if genre == 'anime':
            music_collection.Menambahkan_music(JapanaseAnime(title, artist))
        elif genre == 'rock':
            music_collection.Menambahkan_music(JapanaseRock(title, artist))
        elif genre == 'halal':
            music_collection.Menambahkan_music(HalalMusic(title, artist))
        else:
            print("Genre tidak dikenal. Musik tidak ditambahkan.")
        print("Lagu berhasil ditambahkan")

    elif pilihan == '5':
        artist = input("Masukkan nama penyanyi untuk mencari: ")
        print(f"Musik oleh {artist}:")
        music_collection.search_by_artist(artist)

    elif pilihan == '6':
        title = input("Masukkan judul lagu: ")
        music_collection.delete_music(title)
        print(f"Lagu '{title}' berhasil dihapus.")

    elif pilihan == '0':
        print("Udah duluan ya bre, admin mau berak")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")