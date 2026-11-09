"""""
Nama: Ica Utami Eka Putri
NIM: 2606826
Kelas: 1C
"""""

def selisihWaktu(jamMulai, menitMulai, detikMulai, jamSelesai, menitSelesai, detikSelesai):
    totalMulai = jamMulai * 3600 + menitMulai * 60 + detikMulai
    totalSelesai = jamSelesai * 3600 + menitSelesai * 60 + detikSelesai

    selisih = totalSelesai - totalMulai

    jam = selisih // 3600
    sisa = selisih % 3600
    menit = sisa // 60
    detik = sisa % 60
    return jam, menit, detik

print("Input mulai:")
jam1 = int(input("Jam    : "))
menit1 = int(input("Menit  : "))
detik1 = int(input("Detik  : "))

print("\nInput selesai:")
jam2 = int(input("Jam    : "))
menit2 = int(input("Menit  : "))
detik2 = int(input("Detik  : "))

jam, menit, detik = selisihWaktu(jam1, menit1, detik1, jam2, menit2, detik2)
print(f"\nOutput: {jam} jam - {menit} menit - {detik} detik")