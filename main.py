from life import sehat

print("\n                kalkulator sehat               ")
print("                  by: Taka.py                  ")
print("===============================================")

try:
    nama = str(input("\nNama                    = "))
    umur = float(input ("Umur                    = "))
    kelamin = str(input("Jenis Kelamin [p/l]     = "))
    Tinggi = float(input("Tinggi Badan(Cm)        = "))
    berat = float(input("Berat Badan(Kg)         = "))
    sehat(nama,umur,kelamin,Tinggi,berat)
        
except:
    print('\nInput salah! \nSilahkan coba lagi!')