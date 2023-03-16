"""
Program perulangan membaca buku for
"""

jumlah_buku = 10

print('Ibu berkata, "Baca semua buku!"')

jumlah_buku_yang_sudah_dibaca = 0

# Dengan for
for jumlah_buku_yang_sudah_dibaca in range(1, jumlah_buku+1):
    print(f'Buku Ke-{jumlah_buku_yang_sudah_dibaca} sudah dibaca')

print('=' * 30)

# Tanpa for
print('Buku Ke-1 sudah dibaca')
print('Buku Ke-2 sudah dibaca')
print('Buku Ke-3 sudah dibaca')
print('Buku Ke-4 sudah dibaca')
print('Buku Ke-5 sudah dibaca')
print('Buku Ke-6 sudah dibaca')
print('Buku Ke-7 sudah dibaca')
print('Buku Ke-8 sudah dibaca')
print('Buku Ke-9 sudah dibaca')
print('Buku Ke-10 sudah dibaca')

print('=' * 30)

print('Lapor ke ibu bahwa semua buku sudah dibaca')
