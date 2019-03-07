# Kutuphaneler
import math;

#Fonksiyonlar

def Result(Kisi_Sayisi): #Güvercin Yuvası Prensibi Uygulanıyor ve odadaki toplanan kişi sayısı haftanın 7 gününe bölünür

    result=(math.ceil(int(Kisi_Sayisi)/7.0)) # 7.0 değer haftanın günlerine ait

    return result

def InputKontrolu(GirilenKisiSayisi): # Bir harf girildiğinde veya bir negatif sayı girildiğinde matematik işlemleri yapılmaz hata verir
    value = str(GirilenKisiSayisi)
    if not value.isdigit(): # Girilen değer bir sayı olup olmadığını kontrol ediliyor
        return False
    elif (int(value)<1 ) or (int(value)>96): # Verilen aralık :1 ile 96 kişi arasında olması kontrolu
        return False
    else:
        return True

while True:
    print("Lütfen 1 ile 96 aralığında bir sayı giriniz !!")
    Kisi_Sayisi=input("Odada toplamda kaç kişi bulunmakta ? ")

    if InputKontrolu(Kisi_Sayisi) == True:
        print("Bu grupta en az %d kişinin doğum günü haftanın aynı güne denk gelecektir !!" % Result(Kisi_Sayisi))
    else:
        print("İstenilen aralıkta bir sayı giriniz lütfen !!")
    print("\n")
