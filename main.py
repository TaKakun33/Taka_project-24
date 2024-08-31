import os
from games.yipi import yipi
from mytools.life import *
from games.suit import suit

def user():
    os.system('cls')
    name = input('Silakah tulis nama mu: ')
    while name == '':
        name = input('Input salah! Silakah tulis nama mu: ')
    return name
    
def menu(name):
    try_again = 1
    
    while try_again == 1:
        os.system('cls')
        progarm = input(f'Selamat datang {name}, \nsilahkan pilih menu dibawah ini! \n1. Yipi.Game \n2. Suit.Game \n3. Life.Calc \n0. Exit Program \n>>> ')
        
        while progarm not in ['1','2','3','0']:
            os.system('cls')
            progarm = input(f'Input Salah, \nsilahkan pilih menu dibawah ini! \n1. Yipi.Game \n2. Suit.Game \n3. Life.Calc \n0. Exit Program \n>>> ')
            
        progarm = int(progarm)
        if progarm == 1:
            yipi(name)
        elif progarm == 2:
            suit(name)
        elif progarm == 3:
            bmi(name)
        elif progarm == 0:
            ensure = input('\nProgram akan ditutup! \nKamu yakin! [y/n] \n>>> ')
            if ensure == 'y':
                try_again = 0
        
def exit():
    print('\nShutdown...')
    sleep(1)
    print('3.....')
    sleep(1)
    print('2.....')
    sleep(1)
    print('1.....')
    sleep(1)
    os.system('cls')
    print("Program dihentikan!\n")

def main():
    user_name = user()
    menu(user_name)
    exit()

if __name__ == '__main__':
    main()