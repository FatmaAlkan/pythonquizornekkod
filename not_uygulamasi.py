def not_hesapla(satir):
    satir = satir[:-1]  #sonda 1 boş satırı silmek için
    liste = satir.split(":")    #: ayırız 0 indek ---- isim soyisim bilgisi : 1 index --- not bilgileri
    ogrenci_ad = liste[0]
    not_bilgisi = liste[1].split(",")

    not1 = int(not_bilgisi[0])
    not2 = int(not_bilgisi[1])
    not3 = int(not_bilgisi[2])
    ortalama = (not1 + not2 + not3) /3

    if ortalama >= 90 and ortalama <= 100:
        harf ="AA"
    elif ortalama  >= 85 and ortalama<= 89:
        harf = "BA"
    elif ortalama >= 65:
        harf = "CC"
    else:
        harf ="FF"

    return ogrenci_ad + ": " + harf +"\n"


def ortalama_oku():
    with open("sinav_not.txt", "r", encoding="utf-8") as file :
        for satir in file :
            print(not_hesapla(satir))


def not_gir():
    ad = input("isminizi giriniz: ")
    soyAd = input("soyadinizi giriniz: ")
    not1 = input("1. sinav notunuzu giriniz: ")
    not2 = input("2. sinav notunuzu giriniz: ")
    not3 = input("3. sinav notunuzu giriniz: ")

    with open("sinav_not.txt","a", encoding="utf-8") as file:
        file.write(ad +" " + soyAd + ":" + not1 + "," +not2 + "," + not3 + "\n" )


def not_kayit():
    with open ("sinav_not.txt", "r",encoding="utf-8") as file:
        liste = []

        for i in file :
            liste.append(not_hesapla(i))
        with open("sonuc.txt","w", encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)



while True:
    islem = input(" 1-Notlari oku\n 2-Not gir\n 3-Notlari kayit et\n 4-Cikis\n")

    if islem == "1":
        ortalama_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        not_kayit()
    elif islem == "4":
        break
    else:
        print("hatali giris")
        #break
