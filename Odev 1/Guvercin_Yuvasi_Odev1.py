# Kutuphaneler
import math;

#Fonksiyonlar

def InputKontrolu(GirilenKisiSayisi): # Bir harf girildiğinde veya bir negatif sayı girildiğinde matematik işlemleri yapılmaz hata verir ve kullanıcıdan  bir daha giriş yapılmasını istenir.
    value = str(GirilenKisiSayisi)
    if (int(value)<1 ) or (int(value)>96): # Verilen aralık :1 ile 96 kişi arasında olması kontrolu
        return False 
    elif not value.isdigit(): # Girilen değer bir sayı olup olmadığını kontrol ediliyor
        return False
    else:
        return True
# Ana Fonksiyon
while True:
    print("Lütfen 1 ile 96 aralığında bir sayı giriniz !!")
    Kisi_Sayisi=input("Odada toplamda kaç kişi bulunmakta ? ")

    if InputKontrolu(Kisi_Sayisi) == True: # Kullanıcı tarafindan girilen sayı kriterlerin içinde ise: Güvercin Yuvası Prensibi Uygulanıyor ve odadaki toplanan kişi sayısı haftanın 7 gününe bölünür
        result=(math.ceil(int(Kisi_Sayisi)/7.0))  # 7.0 değer haftanın günlerine ait
        print("Bu grupta en az %d kişinin doğum günü haftanın aynı güne denk gelecektir !!" % Result(Kisi_Sayisi))
    else:
        print("İstenilen aralıkta bir sayı giriniz lütfen !!")
    print("\n")
