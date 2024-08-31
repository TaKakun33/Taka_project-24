def hasil(nama,umur,kelamin,tinggi,berat):
        UMUR = int(umur)
        TINGGI = int(tinggi)
        BERAT = int(berat)
    
        if UMUR > 60 :
            if kelamin == 'l':
                print("Kalori per hari",nama,"  =", (13.5*BERAT)+487, "Kkal")
            if kelamin == 'p':
                print("Kalori per hari",nama,"  =", (10.5*BERAT)+596, "Kkal")

        elif UMUR > 30 :
            if kelamin == 'l':
                print("Kalori per hari",nama,"  =", (11.6*BERAT)+879, "Kkal")
            if kelamin == 'p':
                print("Kalori per hari",nama,"  =", (8.7*BERAT)+829, "Kkal")

        elif UMUR > 18 :
            if kelamin == 'l':
                print("Kalori per hari",nama,"  =", (15.3*BERAT)+679, "Kkal")
            if kelamin == 'p':
                print("Kalori per hari",nama,"  =", (14.7*BERAT)+496, "Kkal")

        elif UMUR > 10 :
            if kelamin == 'l':
                print("Kalori per hari",nama,"  =", (17.5*BERAT)+651, "Kkal")
            if kelamin == 'p':
                print("Kalori per hari",nama,"  =", (12.2*BERAT)+746, "Kkal")

        elif UMUR > 3 :
            if kelamin == 'l':
                print("Kalori per hari",nama,"  =", (22.7*BERAT)+495, "Kkal")
            if kelamin == 'p':
                print("Kalori per hari",nama,"  =", (22.5*BERAT)+499, "Kkal")

        else:
            if kelamin == 'l':
                print("Kalori per hari",nama,"  =", (60.9*BERAT)-54, "Kkal")
            if kelamin == 'p':
                print("Kalori per hari",nama,"  =", (61*BERAT)-51, "Kkal")

        if kelamin == 'l':
            print("Berat Ideal", nama, "      =", (TINGGI - 100)-((TINGGI - 100) * 0.1 ), "Kg")
        elif kelamin == 'p':
            print("Berat Ideal", nama, "      =", (TINGGI - 100)-((TINGGI - 100) * 0.15 ), "Kg")

        imt = BERAT / ((TINGGI/100)**2)
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