import os
import libary.lib_suit as lib
from libary.border import *

def suit(name):
    timer()
    welcome(name,'Suit.Game')
    while True:
        input_player = input('Pilih diantara pilihan ini \ngunting/batu/kertas [1/2/3] \n>>> ')
        try_again = input('\nApakah kamu yakin? [y/n] \n>>> ')

        if try_again == 'n' or input_player not in ['1','2','3']:
            os.system('cls')
            timer()
            welcome(name,'Suit.Game')
            if input_player not in ['1','2','3']:
                print('INPUT SALAH!')
            else:
                print('Silahkan isi kembaili!')
            continue
        
        os.system('cls')
        timer()
        welcome(name,'Suit.Game')
        input_player = int(input_player)
        lib.proses(input_player,name)
                
        try_again = input('\nApakah Mau Ulang Lagi? \n>>> ')
        if try_again == 'y':
            os.system('cls')
            timer()
            welcome(name,'Suit.Game')
            continue
        break

    end(name,1)
    
if __name__ =='__main':
    suit()