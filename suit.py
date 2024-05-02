import random 
from head import head

head('Suit.Game')
translate = {
    1 : 'Gunting',
    2 : 'Batu',
    3 : 'Kertas',
    'g' : 'Gunting',
    'b' : 'Batu',
    'k' : 'Kertas',
}

while True:
    komputer = random.randint(1,3)
    manusia = input('Pilih antara gunting/batu/kertas \n[g/b/k] \n>>> ')
    
    if manusia in ['g','b','k']:
        break
    else:
        head('Suit.Game')
        print('Input salah!')

if komputer == 1 and manusia == 'b' or  komputer == 2 and manusia == 'k' or komputer == 3 and manusia == 'g':
    print(f'\nKomputer: {translate[komputer]}')
    print(f'Kamu: {translate[manusia]}')
    print('kamu menang!')
    
elif komputer == 1 and manusia == 'k' or  komputer == 2 and manusia == 'g' or komputer == 3 and manusia == 'b':
    print(f'\nKomputer: {translate[komputer]}')
    print(f'Kamu: {translate[manusia]}')
    print('kamu kalah!')
   
else:
    print(f'\nKomputer: {translate[komputer]}')
    print(f'Kamu: {translate[manusia]}')
    print('Seri!')
    
print('\nprogram selesai...')