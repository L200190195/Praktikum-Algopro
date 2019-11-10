##Program Akun
##Dibuat Oleh Frischa L200190195
import random
angka=random.randint(0,1000)

Nama = 'Frischa Aura Salsabilla B'
TanggalLahir = '26 Oktober 2001'
NamaSingkat = Nama[0] + "." + Nama[8] + "." + Nama[13:25]
Username = Nama[0] + TanggalLahir[0:2] + TanggalLahir[11:15]
Password = Nama[0:7] + str(angka)

print(Nama)
print(TanggalLahir)
print(NamaSingkat)
print(Username)
print(Password)
