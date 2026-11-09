"""""
Nama: Ica Utami Eka Putri
NIM: 2606826
Kelas: 1C
"""""

def fibonacci(n):

    deret = []
    a = 0
    b = 1
    for i in range(n):
        deret.append(a)
        c = a + b
        a = b
        b = c
    return deret

def volumeTabung(r, t, phi=3.14):
    volume = phi * r * r * t
    return volume

def luasPermukaanTabung(r,t, phi-3.14):
    luas = 2 * phi * r * (r + t)
    return luas

def totalDanRataRata(*angka):
    total = 0
    for i in angka:
        total = total + i
    rataRata = total / len(angka)
    return total, rataRata

print("=== Nomor 1 : Deret Fibonacci ===")
n = int(input("Masukkan banyak suku: "))
if n <= 0:
    print("Jumlah suku harus lebih dari 0!")
else:
    hasil = fibonacci(n)
    print(f"Deret Fibonacci {n} suku: {hasil}")

# nomor 2
print("\n=== Nomor 2 : Volume Tabung ===")
r = float(input("Masukkan jari-jari (r): "))
t = float(input("Masukkan tinggi (t): "))
volume = volumeTabung(r, t)
luas = luasPermukaanTabung(r, t)

print(f"Volume tabung = {volume}")
print(f"Luas permukaan tabung = {luas}")

# nomor 3
print("\n=== Nomor 3 : Total dan Rata-rata ===")
teks = input("Masukkan angka (pisahkan dengan spasi): ")
daftar = teks.split()
angka = []
for i in daftar:
    angka.append(int(i))

total, rataRata = totalDanRataRata(*angka)
print(f"Input    : {angka}")
print(f"Total    : {total}")
print(f"Rata-rata: {rataRata}")