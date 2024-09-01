# desimal ke biner
user = float(input('masukan angka :'))
bit = ''

while(user):
    if user != 1:
        bit = bit + str(int(user % 2))
        user = user // 2
    else:
        bit = bit + '1'
        break
print(bit[::-1])
print(user)