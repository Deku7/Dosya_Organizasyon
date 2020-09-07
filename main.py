import random
import time
from operator import itemgetter

start = time.time()
birincisinif_nosu = 0
ikincisinif_nosu = 0
ucuncusinif_nosu = 0
dorduncusinif_nosu = 0


def erkek_ismi():
    with open("C:\\Users\\berat\\Desktop\\Erkek isimleri.txt") as dosya_erkek:
        isim_erkek = dosya_erkek.read().splitlines()
        a = random.randint(0, 140)
        return isim_erkek[a]


def kiz_ismi():
    with open("C:\\Users\\berat\\Desktop\\Kiz isimleri.txt") as dosya_kiz:
        isim_kiz = dosya_kiz.read().splitlines()
        b = random.randint(0, 110)
        return isim_kiz[b]


def soyisim():
    with open("C:\\Users\\berat\\Desktop\\Soyadlar.txt") as dosya_soyisim:
        soyisim = dosya_soyisim.read().splitlines()
        c = random.randint(0, 240)
        return soyisim[c]


def ganoolusturma():
    rastgelegano = round(random.uniform(0, 4), 3)
    return rastgelegano


def sinifbelirleme():
    rastgelesinif = random.randint(1, 4)
    return rastgelesinif


def ogrenciolustur():
    cinsiyet = random.randint(0, 1)
    if cinsiyet == 0:
        if sinifbelirleme() == 1:
            global birincisinif_nosu
            sinif_nosu = birincisinif_nosu + 1030527500
            birincisinif_nosu += 1
            isim = str(erkek_ismi()) + ' ' + str(soyisim()) + ' ' + str(ganoolusturma()) + ' ' + str(sinif_nosu) + \
                   ' E' + ' 1\n'
            return isim
        elif sinifbelirleme() == 2:
            global ikincisinif_nosu
            sinif_nosu = ikincisinif_nosu + 1030525000
            ikincisinif_nosu += 1
            isim = str(erkek_ismi()) + ' ' + str(soyisim()) + ' ' + str(ganoolusturma()) + ' ' + str(
                sinif_nosu) + ' E' + ' 2\n'
            return isim
        elif sinifbelirleme() == 3:
            global ucuncusinif_nosu
            sinif_nosu = ucuncusinif_nosu + 1030522500
            ucuncusinif_nosu += 1
            isim = str(erkek_ismi()) + ' ' + str(soyisim()) + ' ' + str(ganoolusturma()) + ' ' + str(
                sinif_nosu) + ' E' + ' 3\n'
            return isim
        else:
            global dorduncusinif_nosu
            sinif_nosu = dorduncusinif_nosu + 1030520000
            dorduncusinif_nosu += 1
            isim = str(erkek_ismi()) + ' ' + str(soyisim()) + ' ' + str(ganoolusturma()) + ' ' + str(
                sinif_nosu) + ' E' + ' 4\n'
            return isim
    else:
        if sinifbelirleme() == 1:
            sinif_nosu = birincisinif_nosu + 1030527500
            birincisinif_nosu += 1
            isim = str(kiz_ismi()) + ' ' + str(soyisim()) + ' ' + str(ganoolusturma()) + ' ' + str(
                sinif_nosu) + ' K' + ' 1\n'
            return isim
        elif sinifbelirleme() == 2:
            sinif_nosu = ikincisinif_nosu + 1030525000
            ikincisinif_nosu += 1
            isim = str(kiz_ismi()) + ' ' + str(soyisim()) + ' ' + str(ganoolusturma()) + ' ' + str(
                sinif_nosu) + ' K' + ' 2\n'
            return isim
        elif sinifbelirleme() == 3:
            sinif_nosu = ucuncusinif_nosu + 1030522500
            ucuncusinif_nosu += 1
            isim = str(kiz_ismi()) + ' ' + str(soyisim()) + ' ' + str(ganoolusturma()) + ' ' + str(
                sinif_nosu) + ' K' + ' 3\n'
            return isim
        else:
            sinif_nosu = dorduncusinif_nosu + 1030520000
            dorduncusinif_nosu += 1
            isim = str(kiz_ismi()) + ' ' + str(soyisim()) + ' ' + str(ganoolusturma()) + ' ' + str(
                sinif_nosu) + ' K' + ' 4\n'
            return isim


def bolumsira():
    i = 1
    with open("C:\\Users\\berat\\Desktop\\Kisiler.txt") as kisiler123:
        lines = [line.split(' ') for line in kisiler123]
    output = open("C:\\Users\\berat\\Desktop\\Bolum_Sira.txt", 'w')
    for line in sorted(lines, key=itemgetter(2), reverse=True):
        output.write(str(i))
        output.write('.')
        output.write(' '.join(line))
        i += 1
    output.close()


def sinifsira():
    with open("C:\\Users\\berat\\Desktop\\Bolum_Sira.txt") as kisiler1234:
        lines = [line.split(' ') for line in kisiler1234]
    output = open("C:\\Users\\berat\\Desktop\\Sinif_Sira.txt", 'w')
    for i in range(1, 5):
        k = 1
        for line in lines:
            if int(line.__getitem__(5)) == i:
                output.write(str(k))
                output.write('=')
                output.write(' '.join(line))
                k += 1
    output.close()


def cinsiyetegore():
    with open("C:\\Users\\berat\\Desktop\\Kisiler.txt") as cinsiyet:
        lines = [line.split(' ') for line in cinsiyet]
    outputE = open("C:\\Users\\berat\\Desktop\\Erkek_Ogrenciler.txt", 'w')
    outputK = open("C:\\Users\\berat\\Desktop\\Kiz_Ogrenciler.txt", 'w')
    for line in lines:
        if line.__getitem__(4) == 'K':
            outputK.write(' '.join(line))
        else:
            outputE.write(' '.join(line))
    outputK.close()
    outputE.close()

def Numara_Sirala():
    with open("C:\\Users\\berat\\Desktop\\Kisiler.txt") as kisiler:
        lines = [line.split(' ') for line in kisiler]
    output = open("C:\\Users\\berat\\Desktop\\OgrenciNoSirasi.txt", 'w')
    for line in sorted(lines , key=itemgetter(3)):
        output.write(' '.join(line))
    output.close()


start2 = time.time()
f = open('C:\\Users\\berat\\Desktop\\Kisiler.txt', 'w')
for p in range(10000):
    textList = ogrenciolustur()
    f.write(textList)
f.close()
end2 = time.time()
start3 = time.time()
bolumsira()
end3 = time.time()
start4 = time.time()
sinifsira()
end4 = time.time()
start5 = time.time()
cinsiyetegore()
end5 = time.time()
start6 = time.time()
Numara_Sirala()
end6 = time.time()
end = time.time()
print('toplam geçen süre =', end - start)
print('öğrencileri oluşturma =', end2 - start2)
print('bölümleri sıralama =', end3 - start3)
print('sınıf sırala =', end4 - start4)
print('cinsiyete göre ayırma =', end5 - start5)
print('numaraya göre sıralama =', end6 - start6)

