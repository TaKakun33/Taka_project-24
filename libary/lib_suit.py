import random

def hasil(output = int,nama =str):
    if output == 1:
        print(f'\nselamat, {nama} kamu menang!')
    elif output == 2:
        print(f'\nkamu kalah, {nama}!')
    elif output == 0:
        print(f'\nKamu Seri, {nama}!')
        
def proses(input = int, nama = str):
    ai =random.randint(1,3)
    
    print(f'Computer: {ai}')
    print(f'Pilihan Kamu: {input}')
    
    if input == 1:
        if ai == 1:
            hasil(0,nama)
        elif ai == 2:
            hasil(2,nama)
        elif ai == 3:
            hasil(1,nama)
    elif input == 2:
        if ai == 1:
            hasil(1,nama)
        elif ai == 2:
            hasil(0,nama)
        elif ai == 3:
            hasil(2,nama)
    elif input == 3:
        if ai == 1:
            hasil(2,nama)
        elif ai == 2:
            hasil(1,nama)
        elif ai == 3:
            hasil(0,nama)
            
if __name__ == '__main__':
    proses()