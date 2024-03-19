print("\n                kalkulator sehat               ")
print("                  by: Taka.py                  ")
print("===============================================")

nama = (input("\nNama                    = "))
umur = float(input ("Umur                    = "))
kelamin = str(input("Jenis Kelamin [p/l]     = "))
Tinggi = float(input("Tinggi Badan(Cm)        = "))
berat = float(input("Berat Badan(Kg)         = "))


if umur > 60 :
    if kelamin == 'l':
        print("Kalori per hari",nama,"  =", (13.5*berat)+487, "Kkal")
    elif kelamin == 'p':
        print("Kalori per hari",nama,"  =", (10.5*berat)+596, "Kkal")

elif umur > 30 :
    if kelamin == 'l':
        print("Kalori per hari",nama,"  =", (11.6*berat)+879, "Kkal")
    elif kelamin == 'p':
        print("Kalori per hari",nama,"  =", (8.7*berat)+829, "Kkal")

elif umur > 18 :
    if kelamin == 'l':
        print("Kalori per hari",nama,"  =", (15.3*berat)+679, "Kkal")
    elif kelamin == 'p':
        print("Kalori per hari",nama,"  =", (14.7*berat)+496, "Kkal")

elif umur > 10 :
    if kelamin == 'l':
        print("Kalori per hari",nama,"  =", (17.5*berat)+651, "Kkal")
    elif kelamin == 'p':
        print("Kalori per hari",nama,"  =", (12.2*berat)+746, "Kkal")

elif umur > 3 :
    if kelamin == 'l':
        print("Kalori per hari",nama,"  =", (22.7*berat)+495, "Kkal")
    elif kelamin == 'p':
        print("Kalori per hari",nama,"  =", (22.5*berat)+499, "Kkal")

else:
    if kelamin == 'l':
        print("Kalori per hari",nama,"  =", (60.9*berat)-54, "Kkal")
    elif kelamin == 'p':
        print("Kalori per hari",nama,"  =", (61*berat)-51, "Kkal")


if kelamin == 'l':
    print("Berat Ideal", nama, "      =", (Tinggi - 100)-((Tinggi - 100) * 0.1 ), "Kg")
if kelamin == 'p':
    print("Berat Ideal", nama, "      =", (Tinggi - 100)-((Tinggi - 100) * 0.15 ), "Kg")

imt = berat / ((Tinggi/100)**2)
print("Indeks Masa Tubuh", nama, "=", imt)

if imt >=27.1:
    print("Kategori", nama, "         = Sangat Gemuk")
elif imt >=25.1:
    print("Kategori", nama, "         = Gemuk")
elif imt >=18.5:
    print("Kategori", nama, "         = Normal")
elif imt >=17:
    print("Kategori", nama, "         = Kurus")
else:
    print("Kategori", nama, "         = Sangat Kurus")
    
print("\nProgram telah Selesai! ....")
