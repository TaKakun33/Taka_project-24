# desimal ke biner
user = input('masukan angka :')
bit = ''
underbit = '.'

Split_user = user.split('.')
if len(Split_user)== 2:     
    user_1 = int(Split_user[0])
    user_2 = '0.' + Split_user[1]
    user_2 = float(user_2)
else:
    user_1 = int(Split_user[0])
    user_2 = 0
    underbit = ''
    
while(user_1):
    if user_1 != 1:
        bit = bit + str(user_1 % 2)
        user_1 = user_1 // 2
    else:
        bit = bit + '1'
        break
    
while(user_2):
    user_2 = user_2 * 2
    if user_2 >= 1:
         user_2 = user_2 - 1
         underbit = underbit + '1'
    else:
        underbit = underbit + '0'

bit = bit[::-1]
print(bit)

underbit = '%.18s' % underbit
print(underbit)

biner = bit + underbit
print(biner)