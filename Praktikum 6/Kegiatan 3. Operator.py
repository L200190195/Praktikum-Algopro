Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Frischa Aura Salsabilla B'
>>> NIM = 'L200190195'
>>> x = '1' + NIM[7:]
>>> a = int(x)
>>> b = len(Nama)
>>> 
>>> type(a)
<class 'int'>
>>> #karena nilai dari variabel a telah diubah dari string menjadi integer
>>> type(b)
<class 'int'>
>>> #karena pada variabel b terdapat instruksi 'len'  yang menghasilkan jumlah karakter dari Nama
>>> a/b
47.8
>>> #karena hasil dari 1195 dibagi 24 adalah 47.8 dan '/' merupakan simbol pembagian
>>> a//b
47
>>> #karena hasil dari pembulatan pembagian 1195 dibagi 24 adalah 47 dan '//' merupakan simbol pembulatan pembagian
>>> 10*(a-999)
1960
>>> #karena hasil dari 1195 dikurangi 999 kemudian di kali 10 adalah 1960. '*' merupakan simbol perkalian sedangkan '-' simbol pengurangan
>>> b**2
625
>>> #karena hasil dari 25 dipangkatkan 2 adalah 625. '**' merupakan simbol pangkat
>>> a%b
20
>>> #karena sisa dari pembagian 1195 dibagi 25 adalah 20. '%' merupakan simbol dari operasi sisa hasil pembagian
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> #karena variabel c yaitu "12.5" merupakan angka desimal
>>> a/c
95.6
>>> #karena hasil pembagian 1195 dibagi 12.5 adalah 95.6 dan merupakan data float
>>> a//c
95.0
>>> #karena pembulatan dari pembagian antara 1195 dan 12.5 adalah 95.0
>>> a%c
7.5
>>> #karena sisa hasil bagi dari 1195 dibagi 12.5 adalah 7.5 dan bertipe float
>>> c>b
False
>>> #karena c lebih kecil daripada b dan ">" merupakan operasi yang menghasilkan data logika
>>> type(c>b)
<class 'bool'>
>>> #karena '>' merupakan operasi yang menghasilkan data logika
>>> a > b and b< c
False
>>> #karena 'and' termasuk data logika yang mana True and False akan menghasilkan False
>>> a > 1100 or b< 10
True
>>> #karena 'or' termasuk dalam data logika yang mana True or False menghasilkan True
