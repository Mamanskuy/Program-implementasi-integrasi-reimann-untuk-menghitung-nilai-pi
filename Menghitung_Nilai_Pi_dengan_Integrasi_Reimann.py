print("||    PROGRAM IMPLEMENTASI INTEGRASI     ||")
print("||                RIEMANN                ||")
print("||       UNTUK MENGHITUNG NILAI PI       ||")
print("||   ALMAN KAMAL MAHDI - 21120122120024  ||")
print("||         METODE NUMERIK KELAS B        ||")

import numpy as np
import timeit
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

class AproksimasiPi:
    def __init__(self):
        self.π_referensi = 3.14159265358979323846
        self.N_values = np.array([10, 100, 1000, 10000, 10000, 100000, 1000000])
        self.π_aproksimasi = []
        self.waktu_eksekusi = []
        self.rms_error = []

    def f(self, x):
        return 4 / (1 + x**2)

    def integrasi_riemann(self, a, b, N):
        delta_x = (b - a) / N
        x = np.linspace(a, b, N, endpoint=False) + delta_x / 2
        integral = np.sum(self.f(x)) * delta_x
        return integral

    def hitung_rms_error(self, π_aproksimasi):
        return np.sqrt(mean_squared_error([self.π_referensi] * len(π_aproksimasi), π_aproksimasi))

    def jalankan(self):
        for N in self.N_values:
            waktu_eksekusi = timeit.timeit(lambda: self.integrasi_riemann(0, 1, N), number=100)
            π_aproksimasi = self.integrasi_riemann(0, 1, N)
            
            self.π_aproksimasi.append(π_aproksimasi)
            self.waktu_eksekusi.append(waktu_eksekusi)

            print(f"N = {N}:")
            print(f"Aproksimasi π = {π_aproksimasi}")
            print(f"Waktu Eksekusi = {waktu_eksekusi:.8f} detik")

            rms_error = self.hitung_rms_error([π_aproksimasi])
            self.rms_error.append(rms_error)
            print(f"Error RMS = {rms_error}")
            
            rms_error_persen = (abs(self.π_referensi - π_aproksimasi) / self.π_referensi) * 100
            print(f"Error RMS dalam persentase = {rms_error_persen:.10f}%\n")

        print(f"π Referensi = {self.π_referensi}")

    def plot_aproksimasi_pi(self):
        plt.figure(figsize=(8, 6))
        plt.plot(self.N_values, self.π_aproksimasi, marker='o', color='blue', label='Aproksimasi π')
        plt.axhline(y=self.π_referensi, color='red', linestyle='--', label='π Referensi')
        plt.xscale('log')
        plt.xlabel('N (Jumlah interval)')
        plt.ylabel('Nilai π')
        plt.title('Perbandingan Aproksimasi π dengan Referensi')
        plt.legend()
        plt.grid(True)
        plt.show()

    def plot_error_rms(self):
        plt.figure(figsize=(8, 6))
        plt.plot(self.N_values, self.rms_error, marker='o', color='red', label='Error RMS')
        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel('N (Jumlah interval)')
        plt.ylabel('Error RMS')
        plt.title('Error RMS vs N')
        plt.legend()
        plt.grid(True)
        plt.show()

    def plot_waktu_eksekusi(self):
        plt.figure(figsize=(8, 6))
        plt.plot(self.N_values, self.waktu_eksekusi, marker='o', color='purple', label='Waktu Eksekusi')
        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel('N (Jumlah interval)')
        plt.ylabel('Waktu Eksekusi (detik)')
        plt.title('Perbandingan Waktu Eksekusi dengan N')
        plt.legend()
        plt.grid(True)
        plt.show()

# Menjalankan program
pi_app = AproksimasiPi()
pi_app.jalankan()
pi_app.plot_aproksimasi_pi()
pi_app.plot_error_rms()
pi_app.plot_waktu_eksekusi()
