
def choise(gua,nama,kondisi):
    if kondisi == 1:
        kondisi = 'salah satu gua'
    elif kondisi == 2:
        kondisi = 'kembali'
    else:
        kondisi = 'kembali'
        nama = 'Input salah ' + nama + '!'
        
    output =(input(f'{gua}\n{nama}, Silahkan pilih {kondisi} diantara ke-5 gua di atas, yang diamana terdapat yipi? [1,2,3,4,5]\n>>> '))
    return output
    
def confirm(choise):
    output = input(f'\n{choise}\napakah kamu yakin? [y/n]\n>>> ')
    return output

def hasil(user,choise,yipi,gua,kondisi):
    if kondisi == 1:
        print(f'\n{choise}\nSelamat {user},\nkamu berhasil menemukan yipi di gua no-{yipi}\n{gua}\n')
    else:
        print(f'\n{choise}\nOPPPS,\nkamu salah {user}, yipi berada di gua no-{yipi}\n{gua}\n')
        
if __name__== '__main__':
    choise()
    confirm()
    hasil()
    