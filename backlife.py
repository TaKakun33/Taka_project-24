def sehat(nama,umur,kelamin,tinggi,berat):
    if float(umur) > 60 :
        if kelamin == 'l':
            print("Kalori per hari",nama,"  =", (13.5*float(berat))+487, "Kkal")
        elif kelamin == 'p':
            print("Kalori per hari",nama,"  =", (10.5*float(berat))+596, "Kkal")

    elif float(umur) > 30 :
        if kelamin == 'l':
            print("Kalori per hari",nama,"  =", (11.6*float(berat))+879, "Kkal")
        elif kelamin == 'p':
            print("Kalori per hari",nama,"  =", (8.7*float(berat))+829, "Kkal")

    elif float(umur) > 18 :
        if kelamin == 'l':
            print("Kalori per hari",nama,"  =", (15.3*float(berat))+679, "Kkal")
        elif kelamin == 'p':
            print("Kalori per hari",nama,"  =", (14.7*float(berat))+496, "Kkal")

    elif float(umur) > 10 :
        if kelamin == 'l':
            print("Kalori per hari",nama,"  =", (17.5*float(berat))+651, "Kkal")
        elif kelamin == 'p':
            print("Kalori per hari",nama,"  =", (12.2*float(berat))+746, "Kkal")

    elif float(umur) > 3 :
        if kelamin == 'l':
            print("Kalori per hari",nama,"  =", (22.7*float(berat))+495, "Kkal")
        elif kelamin == 'p':
            print("Kalori per hari",nama,"  =", (22.5*float(berat))+499, "Kkal")

    else:
        if kelamin == 'l':
            print("Kalori per hari",nama,"  =", (60.9*float(berat))-54, "Kkal")
        elif kelamin == 'p':
            print("Kalori per hari",nama,"  =", (61*float(berat))-51, "Kkal")


    if kelamin == 'l':
        print("Berat Ideal", nama, "      =", (float(tinggi) - 100)-((float(tinggi) - 100) * 0.1 ), "Kg")
    if kelamin == 'p':
        print("Berat Ideal", nama, "      =", (float(tinggi) - 100)-((float(tinggi) - 100) * 0.15 ), "Kg")

    imt = float(berat )/ (float(tinggi) **2)
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

if __name__ =="__life__":
    sehat()