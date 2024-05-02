from head import head
from random import randint

while True:
    head("Yepi.Game")
    name = input('Selamat datang di Yepi.game \nSilahkan tulis namamu! \n>>> ')

    title = ' '* int((32 - len(name)) /2)
    head("Yepi.Game")
    print(f'{title}Selamat Datang {name}')

    yepi = randint(1,5)
    
    empty_hole = ['<_>']*5
    hole = empty_hole.copy()
    hole[yepi - 1] = '<^_^>'
    
    empty_hole = ' '.join(empty_hole)
    hole = ' '.join(hole)

    choise = int(input(f'{empty_hole} \nDiantara ke-5, Pilih lubang yang tedapat Yepi di dalamnya! \n>>> '))
    
    sure = input('\nKamu yakin? [y/n] \n>>> ')
    if sure == 'n':
        continue
    
    print(f"\n{hole}")
    
    if yepi == choise:
        print('Selamat Kamu menemukan Yepi!')
    else:
        print(f'Pilhan kamu salah, Yepi berada di {yepi}')
        
    again = input("\nMau Coba lagi?  [y/n] \n>>> ")
    if again == 'n':
        break