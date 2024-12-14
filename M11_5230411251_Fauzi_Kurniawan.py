import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

class QualityAir:
    def __init__(self, data):
        self.data = data
        
        # Memeriksa dan menangani nilai NaN
        if self.data.isnull().values.any():
            print("Data mengandung nilai NaN. Menghapus baris dengan nilai NaN.")
            self.data = self.data.dropna()  # Menghapus baris dengan nilai NaN
        
        # Mengonversi kolom ke tipe data yang sesuai
        self.data = self.data.apply(pd.to_numeric, errors='ignore')
        
        if 'Air Quality' not in self.data.columns:
            raise ValueError("Kolom 'Air Quality' tidak ditemukan dalam data.")
        
        self.X = self.data.drop(['Air Quality'], axis=1)
        self.y = self.data['Air Quality']
        
        # Mengencode label untuk kolom 'Air Quality'
        self.label_encoder = LabelEncoder()
        self.y = self.label_encoder.fit_transform(self.y)
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.train_model()  
    
    @staticmethod
    def Membaca_xlsx(file_path):
        try:
            data = pd.read_excel(file_path)  
            return data
        except FileNotFoundError:
            print("File tidak ditemukan. Pastikan path dan nama file sudah benar.")
            return None
    
    def train_model(self):
        self.model.fit(self.X_train, self.y_train)
        self.y_pred = self.model.predict(self.X_test)
        self.accuracy = accuracy_score(self.y_test, self.y_pred)
        self.classification_report = classification_report(self.y_test, self.y_pred)
        self.confusion_matrix = confusion_matrix(self.y_test, self.y_pred)
        self.plot_confusion_matrix()
    
    def plot_confusion_matrix(self):
        plt.figure(figsize=(10, 6))
        sns.heatmap(self.confusion_matrix, annot=True, fmt='d', cmap='Blues')
        plt.title('Confusion Matrix')
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.show()

class Klasifikasi:
    def __init__(self, data):
        self.data = data
        self.X = data.drop(['Air Quality'], axis=1)
        self.y = data['Air Quality']
        
        # Mengencode label untuk kolom 'Air Quality'
        self.label_encoder = LabelEncoder()
        self.y = self.label_encoder.fit_transform(self.y)
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

    def Regresi_Logistik(self):
        model = LogisticRegression(max_iter=200)
        model.fit(self.X_train, self.y_train)
        y_pred = model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        print("Akurasi Regresi Logistik:", accuracy)
        print("Laporan Klasifikasi:\n", classification_report(self.y_test, y_pred))

    def Bayes_Naif(self):
        model = GaussianNB()
        model.fit(self.X_train, self.y_train)
        y_pred = model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        print("Akurasi Naive Bayes:", accuracy)
        print("Laporan Klasifikasi:\n", classification_report(self.y_test, y_pred))

class Regresi:
    def __init__(self, data):
        self.data = data
        self.X = data.drop(['Air Quality'], axis=1)
        self.y = data['Air Quality']
        
        self.label_encoder = LabelEncoder()
        self.y = self.label_encoder.fit_transform(self.y)
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

    def Linear_Regression(self):
        model = LinearRegression()
        model.fit(self.X_train, self.y_train)
        y_pred = model.predict(self.X_test)
        mse = mean_squared_error(self.y_test, y_pred)
        print("Mean Squared Error (MSE) dari Regresi Linier:", mse)

# Integrate the new class into the main loop
while True:
    print("=" * 50)
    print("{:^50}".format("MENU UTAMA"))  
    print("=" * 50)
    print("1. Membaca XLSX")
    print("2. Training Model")
    print("3. Klasifikasi")
    print("4. Regresi")
    print("5. Exit")
    print("=" * 50)

    pilihan = input("Pilih metode : ")
    
    if pilihan == "1":
        file_name = input("Masukkan nama file XLSX (misal: data.xlsx): ")
        data = QualityAir.Membaca_xlsx(file_name)  
        if data is not None:
            try:
                quality_air = QualityAir(data)  
                print("Data berhasil dimuat.")
                print("\nBeberapa baris pertama dari data:")
                print(quality_air.data.head())  
            except ValueError as e:
                print(e)
        
    elif pilihan == "2":
        if 'quality_air' in locals(): 
            quality_air.train_model() 
            print("Model telah dilatih.")
            print("Akurasi:", quality_air.accuracy)
            print("Laporan Klasifikasi:\n", quality_air.classification_report)
        else:
            print("Silakan muat data terlebih dahulu.")
    
    elif pilihan == "3":
        if 'quality_air' in locals():
            klasifikasi = Klasifikasi(quality_air.data)
            print("Pilih metode klasifikasi:")
            print("1. Regresi Logistik")
            print("2. Bayes Naif")
            klasifikasi_pilihan = input("Pilih metode : ")
            if klasifikasi_pilihan == "1":
                klasifikasi.Regresi_Logistik()
            elif klasifikasi_pilihan == "2":
                klasifikasi.Bayes_Naif()
            else:
                print("Pilihan tidak valid.")
        else:
            print("Silakan muat data terlebih dahulu.")
    
    elif pilihan == "4":
        if 'quality_air' in locals():
            regresi = Regresi(quality_air.data)
            regresi.Linear_Regression()
        else:
            print("Silakan muat data terlebih dahulu.")
    
    elif pilihan == "5":
        print("Keluar dari program.")
        break
    
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")