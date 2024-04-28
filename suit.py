import random 
print("\n                     Suit                      ")
print("                  by: Taka.py                  ")
print("===============================================")

while True:
    komputer = random.randint(1,3)
    manusia = input('Pilih antara gunting/batu/kertas \n[g/b/k]')
    
    if manusia in ['g','b','k']:
        break
    else:
        print('Input salah!')

if komputer == 1 and manusia == 'b' or  komputer == 2 and manusia == 'k' or komputer == 3 and manusia == 'g':
   print('kamu menang!')
    
elif komputer == 1 and manusia == 'k' or  komputer == 2 and manusia == 'g' or komputer == 3 and manusia == 'b':
   print('kamu kalah!')
   
else:
    print('Seri!')
    
print('program selesai...')