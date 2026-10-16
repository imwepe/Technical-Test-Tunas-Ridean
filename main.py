# 1<=N, M<=100
# 1<=Ai<=1000
# 1<=Bi<=1000

N = int(input("Jumlah Lawan: "))
M = int(input("Tingkat Kemahiran: "))

Ai = []
Bi = []

for j in range(N):
    if not M >= Ai:
        M += Bi

### deskripsi alur penghitungan
# baris pertama merupakan jumlah musuh dan level (kemahiran) awal
# baris kedua adalah level musuh
# baris ketiga adalah poin penambahannya (dibaca atas bawah untuk level dan poin tambah)

# contoh output 1
# 1. Juned berada pada level 2 dan harus mengalahkan 4 musuh
# 2. Musuh 1 ada di level 8, Musuh 2 ada di level 9, Musuh 3 ada di level 3, dan Musuh 4 ada di level 2
# 3. Juned hanya bisa mengalahkan musuh yg punya kemampuan sama atau lebih rendah
# 4. Juned harus melawan musuh 4 lebih dulu, sehingga dia bisa mendapatkan 3 poin
# 5. Level Juned berada di level 5 sekarang
# 6. Musuh 3 ada di level 3, sehingga Juned dapat melawan musuh ini dan mendapatkan 1 poin
# 7. Juned sekarang berada di level 6
# 8. Juned tidak dapat melawan siapa-siapa lagi karena Musuh 1 ada di level 8 dan Musuh 2 ada di level 9
# 9. Level Juned berakhir di level 6