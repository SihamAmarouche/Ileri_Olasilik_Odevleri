# Kutuphaneler
import math;

# Fonksiyonlar

def InputKontrolu(GirilenKisiSayisi):  # Bir harf girildiğinde veya bir negatif sayı girildiğinde matematik
    # işlemleri yapılmaz hata verir ve kullanıcıdan  bir daha giriş yapılmasını istenir.
    value = GirilenKisiSayisi
    if not value.isdigit():  # Girilen değer bir sayı olup olmadığını kontrol ediliyor
        return False
    elif (int(value) == 0):
        return 3
    elif (int(value) < 7) or (int(value) > 500):  # Verilen aralık : 7 ile 500 kişi arasında olması kontrolu
        return False
    else:
        return True


# Ana Fonksiyon

while True:
    print("Lütfen 7 ile 500 aralığında bir sayı giriniz, Programı durdurmak için 0 numarasına basınız!!")
    Kisi_Sayisi = input("Odada toplamda kaç kişi bulunmakta ? ")

    if InputKontrolu(
            Kisi_Sayisi) == True:  # Kullanıcı tarafindan girilen sayı kriterlerin içinde ise: Güvercin Yuvası Prensibi Uygulanıyor ve odadaki toplanan kişi sayısı haftanın 7 gününe bölünür
        result = (math.ceil(int(Kisi_Sayisi) / 7.0))  # 7.0 değer haftanın günlerine ait
        print("Bu grupta en az %d kişinin doğum günü haftanın aynı güne denk gelecektir !!" %result)
    elif InputKontrolu(Kisi_Sayisi) == 3:
        print("Program Durduruldu !!")
        break;
    else:
        print("\nLütfen istenilen aralıkta bir sayı giriniz!!")
    print("\n")
