import numpy as np
import time
from scipy.integrate import simps

# Fungsi target untuk diintegrasikan
def target_function(x):
    return 4 / (1 + x**2)

# Metode integrasi Riemann
def riemann_sum(N):
    dx = 1.0 / N
    x = np.arange(0, 1, dx)
    return np.sum(target_function(x)) * dx

# Metode integrasi Trapezoid
def trapezoidal_rule(N):
    x = np.linspace(0, 1, N + 1)
    y = target_function(x)
    return np.trapz(y, x)

# Metode integrasi Simpson
def simpson_rule(N):
    x = np.linspace(0, 1, N + 1)
    y = target_function(x)
    return simps(y, x)

# Fungsi untuk menghitung galat kuadrat rata-rata (RMS)
def rms_error(approximation, exact_value):
    return np.sqrt((approximation - exact_value)**2)

# Nilai eksak dari pi
exact_pi = np.pi

# Daftar variasi nilai N
N_list = [10, 100, 1000, 10000]

def main():
    # Meminta masukan NIM dari pengguna
    nim = input("Masukkan NIM Anda: ")
    if len(nim) < 2:
        print("NIM minimal dua digit.")
        return

    # Mendapatkan dua digit terakhir dari NIM
    last_two_digits = int(nim[-2:])
    selected_method = last_two_digits % 3

    # Menentukan metode integrasi berdasarkan digit terakhir NIM
    if selected_method == 0:
        method_name = "Riemann"
        integration_function = riemann_sum
    elif selected_method == 1:
        method_name = "Trapezoid"
        integration_function = trapezoidal_rule
    else:
        method_name = "Simpson"
        integration_function = simpson_rule

    print(f"Metode yang digunakan: {method_name}")

    # Menyimpan hasil
    results = []

    for N in N_list:
        start = time.time()
        result = integration_function(N)
        duration = time.time() - start
        error = rms_error(result, exact_pi)

        results.append({
            'N': N,
            'Result': result,
            'Error': error,
            'Time': duration
        })

    # Menampilkan hasil
    for res in results:
        print(f"N = {res['N']}")
        print(f"Result = {res['Result']}, Error = {res['Error']}, Time = {res['Time']}")
        print()

if __name__ == "__main__":
    main()
