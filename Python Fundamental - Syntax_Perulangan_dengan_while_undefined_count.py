"""
Program perulangan membaca buku dengan while_undefined_count
"""

jumlah_buku = 10
print(f'Jumlah buku {jumlah_buku}')
print('Ibu berkata, "Baca semua buku sampai paham"')
print('Anak menjawab, "OK"')

jumlah_paham = 0
print(f'Jumlah buku yang dipahami {jumlah_paham}')

total_jumlah_baca = 0

while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_paham == 9:
        print(f'Buku ke-{jumlah_paham + 1} belum paham')
    else:
        jumlah_paham = jumlah_paham + 1
        print(f'Buku ke-{jumlah_paham} sudah dipahami')

print(f'Jumlah buku yang bisa dipahami {jumlah_paham}')

if jumlah_paham == jumlah_buku:
    print('Lapor ke ibu bahwa semua buku sudah dipahami')
else:
    print(f'Lapor ke ibu bahwa tidak semua buku bisa dipahami. Si anak hanya bisa memahami {jumlah_paham} buku')
