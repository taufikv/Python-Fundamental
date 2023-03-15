"""
Semua sistaksis dasar bahasa pemograman terdiri dari:
1. Sequential : langkah berurutan
2. Percabangan : langkah melompat jika kondisi terpenuhi
3. Perulangan : mengulang langkah berkali-kali selama/sampai kondisi terpenuhi
"""

# Sequential : langkah berurutan
print('\n===Sequential: Langkah berurutan===\n')
print('Ibu berkata, "Pergi ke toko"')
print('Anak menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli 1 botol susu, dan jika ada telur beli 6 butir"')
print('Maka si anak pergi ke toko')
print('Dan mulai berbelanja')

# Percabangan : Langkah melompat jika kondisi terpenuhi
print('\n\n===Percabangan : Langkah melompat jika kondisi terpenuhi===\n')

print('Ibu berkata, "Beli 1 botol susu dan 6 butir telur"')
print('Anak menjawabm "OK"')
print('Maka anak pergi ke toko')
print('Dan mulai berbelanja')

print('=' * 30)

jumlah_botol_susu = 100
jumlah_telur      = 1446
print(f'Jumlah botol susu {jumlah_botol_susu} botol')
print(f'Jumlah telur {jumlah_telur} butir')

print('=' * 30)

if jumlah_botol_susu > 0:
    print('Anak mengecek harganya, dan ternyata uangnya cukup')
    if jumlah_telur == 0:
        print('Anak membeli 1 botol susu')
    else:
        print('Anak membeli 1 botol susu dan 6 butir telur')
else:
    print('Anak tidak jadi membeli susu')

print('Anak pulang kerumah')
print('Menyerahkan hasil belanjanya kepada Ibu')
