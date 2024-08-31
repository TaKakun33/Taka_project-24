from time import sleep
import os

def timer():
    print('\nTunggu sebentar...')
    sleep(1)

def welcome(user_name, progarm_name): 
    bingkai = '=' * (len(user_name) + len(progarm_name) + 41)
    os.system('cls')
    print (f'{bingkai}\n===========Selamat datang {user_name} di {progarm_name}===========\n{bingkai}\n')

def end(user_name = str,progarm = int):
    if progarm == 2:
        progarm_name = 'Yipi.Game'
        teks = 'The First Weahlt Is Health'
    elif progarm == 1:
        progarm_name = 'Life.Calc'
        teks = 'Game Tamat!'
    elif progarm == 3:
        progarm_name = 'Face.Cam'
        teks = 'Camera berhenti!'
        
    panjang = int(len(user_name)  + len(progarm_name) + 41)
    bingkai = '=' * panjang
    teks = teks + '' *(panjang -len(teks))
    
    print(f'\n{bingkai}\n{teks}\n')
    
    print('akan menutup program dalam hitungan')
    sleep(1)
    print('3.....')
    sleep(1)
    print('2.....')
    sleep(1)
    print('1.....')
    sleep(1)
    
