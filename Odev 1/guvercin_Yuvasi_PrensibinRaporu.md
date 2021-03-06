

### GÜVERCİN YUVASI PRENSİBİ :

Bilgisayar bilimleri de dahil olmak üzere pek çok matematik temelli bilim ve mühendislik alanında kullanılan oldukça basit bir umdedir. İsmini güvercin yuvalarından alan bu kaideye göre yuva sayısından fazla güvercin varsa, ve bütün güvercinler bir yuvaya girecekse, en az bir yuvaya birden fazla güvercin girmek zorundadır.

##### Matematiksel Gösterimi :
Bu durumu sembollerle göstermemiz gerekirse n tane yuva ve m tane güvercin için :
m > n durumunda en az bir yuvada birden fazla güvercin bulunmalıdır.



![pigeon](https://user-images.githubusercontent.com/10710980/54494415-121e4980-48eb-11e9-95e9-33fc19a288f2.png)




Örnek :

Bir Odada 8 kişi toplandığını düşünelim, en az kaç kişinin doğum günü haftanın aynı güne denk gelecektir ? 

Cevap : 2 kişidir.

=============

Çözüm :

8 kişi haftanın 7 gününe ayrılacaktır.
Güvercin Yuvası Prensibine uyarlandığında güvercin sayısı kişi sayısı ile; haftanın 7 günü ise yuva sayısı ile özdeleştirilmiştir.

Kişi sayısı, haftanın günlerin sayısına (yani burada 7'e) bölünür. Sonra bulunan değer yukarıya yuvarlanır.

=============



##### Yukarıdaki örneğin matematiksel çözümü :

Ornek_cozumu.py
```python
math.ceil(Güvercin sayısı / Yuva sayısı)= math.ceil(Kişi sayısı / Haftanın gün sayısı)
## örneğin :
math.ceil(8/7)=2
```

###### Seçtiğim Senaryonun Python Kodları Aşağıdaki Gibidir:

Odev1.py
```python
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


```

###### Referanslar:
* http://bilgisayarkavramlari.sadievrenseker.com/2009/12/10/guvercin-yuvasi-kaidesi-pigeonhole-principle/
* https://www.matematiksel.org/guvercin-yuvasi-prensibi/
