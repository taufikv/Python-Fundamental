"""
Program perulangan membaca buku dengan while
"""

jumlah_buku = 10
print(f'Jumlah buku {jumlah_buku}')
print('Ibu berkata, "Baca semua buku"')
print('Anak menjawab, "OK"')

jumlah_buku_yang_sudah_dibaca = 0
print(f'Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')

while jumlah_buku_yang_sudah_dibaca < jumlah_buku:
    jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca + 1
    print(f'Buku ke-{jumlah_buku_yang_sudah_dibaca} sudah dibaca')

print(f'Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}')
print('Lapor ke ibu semua buku sudah dibaca')
