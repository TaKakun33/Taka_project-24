user = input('masukan biner:')

jumlah_bit = len(user) - 1
deci = 0

for i in user:
        if i == '1':
            deci = deci + 2**(jumlah_bit)
            jumlah_bit = jumlah_bit - 1
        elif i == '0':
            deci = deci + 0
            jumlah_bit = jumlah_bit - 1

print(deci)

