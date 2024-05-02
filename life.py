from backlife import sehat
from head import head

head('Life.Calc')
while True:
    try:
        nama = str(input("Nama                    = "))
        umur = float(input ("Umur                    = "))
        kelamin = str(input("Jenis Kelamin [p/l]     = "))
        
        if kelamin not in ['p','l']:
            Eror = int("fdg")
        
        Tinggi = float(input("Tinggi Badan(Cm)        = "))
        berat = float(input("Berat Badan(Kg)         = "))
        
        sehat(nama,umur,kelamin,Tinggi,berat)
        break
            
    except ValueError:
        head('Life.Calc')
        print('Input salah! \nSilahkan coba lagi!')
