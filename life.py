from backlife import sehat
from head import head

head('Life.Calc')

try:
    nama = str(input("Nama                    = "))
    umur = float(input ("Umur                    = "))
    kelamin = str(input("Jenis Kelamin [p/l]     = "))
    Tinggi = float(input("Tinggi Badan(Cm)        = "))
    berat = float(input("Berat Badan(Kg)         = "))
    sehat(nama,umur,kelamin,Tinggi,berat)
        
except:
    print('\nInput salah! \nSilahkan coba lagi!')