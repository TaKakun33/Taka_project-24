import os
from libary.border import *
from libary.lib_life import hasil


def bmi(nama):
    try_again = 'y'
    loop = 'n'
    Try = 'y'
    
    while try_again == 'y':
        timer()
        welcome(nama,'Life.Calc')
        
        if loop == 'y':
            Try = 'n'
            print('Input Salah!')
        if Try == 'n':
            print('Silahkan ulang kembali!')
            
        print(f'{nama}, Isi data dibawah ini!')
        
        umur = (input ("Umur                    = "))
        kelamin = (input("Jenis Kelamin           = "))
        Tinggi = (input("Tinggi Badan(Cm)        = "))
        berat = (input("Berat Badan(Kg)         = "))
        Try = input('\nApakah sudah yakin? [y/n] \n>>> ')
        
        angka = list(range(0,1000))
        angka = [str(x) for x in angka]    
        
        if Try == 'n':
            continue
        if umur and Tinggi and berat not in angka or kelamin not in ['l','p']:
            loop = 'y'
            continue
        
        timer()
        welcome(nama,'Life.Calc')
        hasil(nama,umur,kelamin,Tinggi,berat)
    
        try_again = input('\ncoba lagi? [y/n] \n>>> ')
        if try_again == 'n':
            end(nama,2)
        loop = 'n'

if __name__ == "__main__":
    bmi()
