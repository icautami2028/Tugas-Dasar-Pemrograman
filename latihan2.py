"""""
Nama: Ica Utami Eka Putri
NIM: 2606826
Kelas: 1C
"""""

def login():
    passwordBenar = "Latihan"
    kesempatan = 3

    username = input("Username : ")

    while kesempatan > 0:
        password = input("Password : ")
        if password == passwordBenar:
            print(f"Login berhasil, selamat datang {username}!")
            return True
        else:
            kesempatan = kesempatan - 1
            if kesempatan > 0:
                print(f"Password salah! Sisa kesempatan: {kesempatan}")
            else:
                print("Password salah! Kesempatan habis, keluar dari menu login.")
    return False

print("=== LOGIN ADMIN ===")
login()