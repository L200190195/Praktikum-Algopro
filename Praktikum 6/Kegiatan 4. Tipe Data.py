Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Frischa Aura Salsabilla B'
>>> NIM = 195
>>> Tinggi = 1,55
>>> Berat = 41
>>> TahunLahir = 2001
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> 
>>> type(Aku)
<class 'tuple'>
>>> #karena tipe dari variabel Aku adalah 'tuple' yang ditandai dengan tanda kurung biasa
>>> Aku[0]
2001
>>> #karena karakter ke-0 dari variabel 'Aku' adalah TahunLahir yang berisi 2001
>>> a = NIM % 4 ; Aku[a]
195
>>> #karena variabel a berisi nilai dari sisa hasil bagi 195 dibagi 4 yaitu 3, kemudian menampilkan karakter/indeks ke-3 dari variabel Aku yaitu NIM : 195
>>> type(Aku[a])
<class 'int'>
>>> #karena tipe data dari indeks/ karakter ke-3 dari variabel 'Aku' yaitu NIM berupa angka integer atau bilangan bulat
>>> Aku[a:4]
(195,)
>>> #karena intruksi memerintahkan untuk menampilkan indeks ke-3 sampai indkes ke-3 jadi yang dihasilkan adalah NIM 195,
>>> type (Aku[4])
<class 'str'>
>>> #karena indeks ke-4 dari variabel 'Aku' adalah Nama, dan tipe data dari 'Nama' itu sendiri adalah string karena diapit 2 tanda petik
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> #karena tipe data tuple itu tidak bisa diubah sehingga saat indeks ke-0 dari data tuple pada variable Aku diganti menjadi 'ok' hasil yang muncul adalah typeError
>>> type(Data)
<class 'list'>
>>> #karena tipe dari variabel Data adalah ' list' yang ditandai dengan tanda kurung siku
>>> type(Data[4])
<class 'str'>
>>> #karena indeks ke-4 dari variabel 'Data' adalah 'Nama' yang mana 'Nama' itu bertipe string ditandai dengan diapit oleh 2 tanda petik
>>> Data [4][5]
'h'
>>> #karena indeks ke-4 dari variabel 'Data' adalah 'Nama' dan karakter ke-5 dari variabel 'Nama' adalah huruf 'h'
>>> Data[4][a:6]
'sch'
>>> #karena indeks ke-4 dari 'Data' adalah 'Nama', dan indeks atau karakter dari karakter ke-2 sampai ke-5 dari variabel 'Nama' itu sendiri adalah sch
>>> Data[0] = 'ok' ; Data
['ok', 41, (1, 55), 195, 'Frischa Aura Salsabilla B']
>>> #karena tipe dari Data adalah list sehingga isinya dapat diubah, yaitu indeks ke-0 diubah dari 2001 menjadi 'ok' dan semua isi dari list variabel Data di tampilkan
>>> Data[-a]
(1, 55)
>>> #karena nilai dari variabel a adalah 3 maka Data[-3] merujuk pada indeks ke-3 dari list Data yang dimulai dari sebelah kanan, sehingga Data[-a] adalah tinggi yaitu 1,55
>>> range(a)
range(0, 3)
>>> #karena range dari a yang bernilai 3 itu adalah (0,3) yang berisi (0,1,2)
