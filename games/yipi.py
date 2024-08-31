import random
import os
from  libary.libary_yipi import *
from libary.border import *


def yipi(nama_user):

    confirm_user ='n'  # untuk melooping
    try_again = 'y'
        
    while confirm_user == 'n' or try_again == 'y':    # apabila masih n

        yipi = random.randint(1,5)
        
        empty_gua = ['<_>']*5
        gua = empty_gua.copy()
        gua[yipi - 1] = '<^_^>'
        
        empty_gua = ' '.join(empty_gua)
        gua = ' '.join(gua)
        timer()
        welcome(nama_user,'Yipi.Game')
        input_user = choise(empty_gua,nama_user,1)
        
        while input_user not in {'1','2','3','4','5'}:
            welcome(nama_user,'Yipi.Game')
            input_user = choise(empty_gua,nama_user,3)
            
        your_choise = f'pilihanmu no-{input_user}'
        input_user = int(input_user)
        confirm_user = confirm(your_choise)
            
        while confirm_user == 'n':
            welcome(nama_user,'Yipi.Game')
            input_user = choise(empty_gua,nama_user,2)
            while input_user not in {'1','2','3','4','5'}:
                os.system('cls')
                welcome(nama_user,'Yipi.Game')
                input_user = choise(empty_gua,nama_user,3)
            your_choise = f'pilihanmu no-{input_user}'
            input_user = int(input_user)
            confirm_user = confirm(your_choise)
    # jika n dia akan ulang dari awal
        
        if confirm_user == 'y':
            if input_user == yipi:
                hasil(nama_user,your_choise,yipi,gua,1)
                try_again = input('Mulai game baru? [y/n]\n>>>') 
                    
            else:
                hasil(nama_user,your_choise,yipi,gua,2)
                try_again = input('Coba Lagi? [y/n]\n>>> ')
    end(nama_user,1)
    #game tamat!
    
if __name__ == '__main__':
    yipi()