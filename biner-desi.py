user = input('masukan biner:')

underdeci = 0
deci = 0

Split_user = user.split('.')
if len(Split_user)== 2:     
    user_1 = Split_user[0]
    user_2 = Split_user[1]
else:
    user_1 = Split_user[0]
    user_2 = ''
    
jumlah_bit = len(user_1) - 1
for i in user_1:
        if i == '1':
            deci = deci + 2**(jumlah_bit)
            jumlah_bit = jumlah_bit - 1
        elif i == '0':
            deci = deci + 0
            jumlah_bit = jumlah_bit - 1
        
jumlah_bit = 1
for i in user_2:
    if i == '1':
        underdeci = underdeci + 2**(-jumlah_bit)
        jumlah_bit = jumlah_bit + 1
    elif i == '0':
        underdeci = underdeci + 0
        jumlah_bit = jumlah_bit + 1
        
print(user_1)
print(underdeci)
print(deci)

